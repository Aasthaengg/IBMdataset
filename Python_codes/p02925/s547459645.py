import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())

    # id table
    N=0
    id=[[None]*n for _ in range(n)]
    from itertools import product
    for i,j in product(range(n),repeat=2):
        if(i>=j): continue
        id[i][j]=N
        N+=1
    toID=lambda i,j:id[min(i,j)][max(i,j)]

    E=[[] for _ in range(N)]
    for i in range(n):
        A=list(map(lambda x:int(x)-1,input().split()))
        for j in range(n-2):
            u=toID(i,A[j])
            v=toID(i,A[j+1])
            E[u].append(v)

    # longest path problem
    dp=[-1]*N
    def dfs(v):
        if(dp[v]>=0): return dp[v]
        dp[v]=-2
        res=0
        for nv in E[v]:
            if(dp[nv]==-2):
                print(-1)
                exit()
            res=max(res,dfs(nv)+1)
        dp[v]=res
        return res

    print(max(dfs(v) for v in range(N))+1)
resolve()