H,W,D=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
dic={}
for i in range(H):
    for j in range(W):
        dic[A[i][j]]=(i,j)
dist=[0]*(H*W+10)
for i in range(D+1,H*W+1):
    xd=abs(dic[i][0]-dic[i-D][0])
    yd=abs(dic[i][1]-dic[i-D][1])
    dist[i]=dist[i-D]+xd+yd
Q=int(input())
for i in range(Q):
    L,R=map(int,input().split())
    print(dist[R]-dist[L])