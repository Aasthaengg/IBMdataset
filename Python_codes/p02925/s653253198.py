import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    N=0
    id=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            id[i][j]=N
            N+=1
    to_id=lambda i,j:id[min(i,j)][max(i,j)]

    E=[[] for _ in range(N)]
    for i in range(n):
        A=tuple(map(int,input().split()))
        for j in range(n-2):
            u=to_id(i,A[j]-1)
            v=to_id(i,A[j+1]-1)
            E[u].append(v)

    # longest path problem
    dp=[None]*N

    def dfs(v):
        if(dp[v] is not None): return dp[v]
        dp[v]=-1
        res=0
        for nv in E[v]:
            if(dp[nv]==-1):
                print(-1)
                exit(0)
            res=max(res,dfs(nv)+1)
        dp[v]=res
        return res

    print(max(dfs(v) for v in range(N))+1)
resolve()