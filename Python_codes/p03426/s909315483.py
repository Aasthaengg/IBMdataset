from bisect import *
H,W,D=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
zahyou=[[0,0] for i in range(H*W+1)]
for h in range(H):
    for w in range(W):
        zahyou[A[h][w]][0]=h
        zahyou[A[h][w]][1]=w
dp=[0 for i in range(H*W+1)]
for i in range(len(dp)):
    if i>=D:
        A1=zahyou[i][0]-zahyou[i-D][0]
        A2=zahyou[i][1]-zahyou[i-D][1]
        if A1<0:A1=-A1
        if A2<0:A2=-A2
        dp[i]=dp[i-D]+A1+A2

for i in range(int(input())):
    l,r=map(int,input().split())
    print(dp[r]-dp[l])
