# longest path

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def main():
    N, M = map(int, input().split())
    edge = defaultdict(lambda: [])

    memo = [0] * 110000
    done = [False] * 110000

    def dp(v):
        if done[v]:
            return memo[v]
        ans = 0
        for to in edge[v]:
            ans = max(ans, dp(to) + 1)
        done[v] = True
        memo[v] = ans
        return ans

    for i in range(M):
        u, v = map(int, input().split())
        edge[u].append(v)

    ans = 0
    for v in range(1, N + 1):
        ans = max(ans, dp(v))
    print(ans)


if __name__ == "__main__":
    main()
