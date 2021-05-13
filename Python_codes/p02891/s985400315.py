import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
from collections import deque
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    S = readline().decode('utf-8').strip()
    K = int(readline())
    L = len(S)

    continuous = deque()

    count = 0
    last = ''
    for i in range(L):
        if i == 0:
            last = S[i]
            count += 1
        else:
            if last==S[i]:
                count += 1
            else:
                continuous.append(count)
                count = 1
                last = S[i]
    continuous.append(count)

    ans = 0
    if len(continuous)==1:
        ans = L*K//2
    else:
        if S[0]==S[-1]:
            a = continuous.popleft()
            b = continuous.pop()
            ans += ((a+b)//2)*(K-1) + a//2 + b//2
        while continuous:
            a = continuous.popleft()
            ans += a//2*K
    print(ans)

if __name__ == '__main__':
    main()
