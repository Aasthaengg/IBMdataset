import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    S=list(map(int,input().split()))
    T=list(map(int,input().split()))
    C=[[0]*(m+1) for _ in range(n+1)] # dp の累積和を持つ
    for i in range(n): C[i][0]=1
    for j in range(m): C[0][j]=1

    for i in range(n):
        for j in range(m):
            if(S[i]==T[j]): C[i+1][j+1]+=C[i][j]
            C[i+1][j+1]+=C[i+1][j]+C[i][j+1]-C[i][j]
            C[i+1][j+1]%=MOD

    print((C[-1][-1]+2)%MOD)
resolve()