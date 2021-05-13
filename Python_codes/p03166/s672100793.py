import sys
sys.setrecursionlimit(10 ** 7)

def resolve():
    def rec(v):
        if dp[v] != -1:
            return dp[v]
        res = 0
        for nv in G[v]:
            res = max(res, rec(nv)+1)
        dp[v] = res
        return res

    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(lambda x:int(x)-1, input().split())
        G[x].append(y)

    dp = [-1]*N
    ans = 0
    for v in range(N):
        ans = max(ans, rec(v))
    print(ans)


if __name__ == "__main__":
    resolve()
