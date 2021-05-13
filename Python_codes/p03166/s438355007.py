from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def main():
    N, M = list(map(int, input().split(' ')))
    adj_nodes = defaultdict(list)
    for _ in range(M):
        x, y = list(map(int, input().split(' ')))
        x -= 1
        y -= 1
        adj_nodes[x].append(y)
    dp = [-1 for _ in range(N)]

    def rec(v):
        if dp[v] >= 0:
            return dp[v]
        ret = 0
        for nv in adj_nodes[v]:
            ret = max([ret, rec(nv) + 1])
        dp[v] = ret
        return ret

    ans = 0
    for v in range(N):
        ans = max([ans, rec(v)])
    print(ans)


if __name__ == '__main__':
    main()
