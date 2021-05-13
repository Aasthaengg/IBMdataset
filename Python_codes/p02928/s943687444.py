import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] > A[j]:
                if i < j:
                    ans += K * (K + 1) // 2
                else:
                    ans += K * (K - 1) // 2
                ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
