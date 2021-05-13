import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    B = list(map(int, readline().split()))
    ans = []
    for _ in range(N):
        L = len(B)
        k = -1
        for i in range(L):
            if B[i]==i+1:
                k = i
        if k == -1:
            print('-1')
            sys.exit()
        else:
            ans.append(B.pop(k))
    for i in range(N)[::-1]:
        print(ans[i])

if __name__ == '__main__':
    main()