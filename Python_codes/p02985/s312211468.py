N,K=map(int,input().split())
A=[list(map(int,input().split())) for i in range(N-1)]
m=10**9+7
c=[[] for i in range(N)]
for i,j in A:
    c[i-1].append(j-1)
    c[j-1].append(i-1)
import sys
sys.setrecursionlimit(10**6)
def bfs(p):
    r=K
    d=1
    n=[1]*N
    while len(p)>0:
        q=[]
        for e in p:
            n[e]=0
            x=max(K-min(2,d),0)
            for f in c[e]:
                if n[f]:
                    q.append(f)
                    r=(r*x)%m
                    x-=1
        p=q
        d+=1
    return r
print(bfs([A[0][0]-1]) if N>1 else K)