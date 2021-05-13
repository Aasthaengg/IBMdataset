import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    A=[[INF]*n for _ in range(n)]
    for i in range(n):
        A[i][i]=0
    ABC=[None]*m
    for i in range(m):
        a,b,c=map(int,input().split())
        a-=1; b-=1
        A[a][b]=c; A[b][a]=c
        ABC[i]=(a,b,c)

    from itertools import product
    for k,i,j in product(range(n),repeat=3):
        A[i][j]=min(A[i][j],A[i][k]+A[k][j])

    ans=0
    for a,b,c in ABC:
        ans+=all(A[u][v]<A[u][a]+c+A[b][v] for u,v in product(range(n),repeat=2))
    print(ans)
resolve()