from sys import setrecursionlimit
setrecursionlimit(10 ** 7)


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())
        graph[x].append(y)
    dp = [-1 for _ in range(n)]
    # dp[i] := iから距離が最も長い頂点への距離

    def solve(v):
        if dp[v] != -1:
            return dp[v]
        res = 0
        for next_v in graph[v]:
            res = max(res, solve(next_v) + 1)
        dp[v] = res
        return dp[v]

    ans = 0
    for i in range(n):
        ans = max(ans, solve(i))
    print(ans)


if __name__ == '__main__':
    main()
