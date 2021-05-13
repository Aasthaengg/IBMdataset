import sys
input = sys.stdin.readline
N,M,L=map(int,input().split())

def war(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
INF=(L+1)*N
d=[[INF]*N for _ in range(N)]
d2=[[INF]*N for _ in range(N)]

for _ in range(M):
    A,B,C=map(int,input().split())
    if C>L:
        continue
    d[A-1][B-1]=C
    d[B-1][A-1]=C

for i in range(N):
    d[i][i]=0

d=war(d)

for i in range(N):
    for j in range(N):
        if d[i][j]<=L:
            d2[i][j]=1
for i in range(N):
    d2[i][i]=0
d2=war(d2)
#print(d)
#print(d2)
Q=int(input())
for i in range(Q):
    s,t=map(int,input().split())
    print(d2[s-1][t-1] %INF -1)
