import sys
from collections import deque
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    X = readline().decode('utf-8').strip()
    L = len(X)
    S = X[0]
    count = 0
    RLE = []
    for i in range(L):
        if X[i] == S:
            count += 1
        else:
            RLE.append((S,count))
            S = X[i]
            count = 1
        if i==L-1:
            RLE.append((S,count))
    d = deque(RLE)
    if d[0][0] == 'T':
        d.popleft()
    if d[-1][0] == 'S':
        d.pop()
    s = 0
    t = 0
    count = 0
    while d:
        s += d.popleft()[1]
        t = d.popleft()[1]
        if s>=t:
            count += t*2
            s -= t
        else:
            count += s*2
            s = 0
    ans = L-count
    print(ans)


if __name__ == '__main__':
    main()