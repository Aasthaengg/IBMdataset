import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,k=map(int,input().split())
    X=[0]*n
    Y=[0]*n
    for i in range(n):
        X[i],Y[i]=map(int,input().split())
    ans=INF
    for a in range(n):
        for b in range(n):
            for c in range(a+1,n):
                for d in range(b+1):
                    x0,x1=sorted([X[a],X[c]])
                    y0,y1=sorted([Y[b],Y[d]])
                    count=0
                    for i in range(n):
                        if x0<=X[i]<=x1 and y0<=Y[i]<=y1:
                            count+=1
                    if count>=k:
                        ans=min(ans,(x1-x0)*(y1-y0))
    print(ans)
resolve()