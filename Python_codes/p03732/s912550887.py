import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,W=map(int,input().split())
    w0,v=map(int,input().split())
    V=[[] for _ in range(4)]
    V[0].append(v)
    for _ in range(n-1):
        w,v=map(int,input().split())
        V[w-w0].append(v)
    for i in range(4):
        V[i].sort(reverse=1)
        V[i].insert(0,0)
        for j in range(len(V[i])-1):
            V[i][j+1]+=V[i][j]

    ans=0
    from itertools import product
    for a,b,c,d in product(range(len(V[0])),range(len(V[1])),range(len(V[2])),range(len(V[3]))):
        v=V[0][a]+V[1][b]+V[2][c]+V[3][d]
        if(a*w0+b*(w0+1)+c*(w0+2)+d*(w0+3)<=W): ans=max(ans,v)
    print(ans)
resolve()