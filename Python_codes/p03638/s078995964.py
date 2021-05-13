# coding: utf-8
H,W=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))

ans=[[0 for i in range(W)] for j in range(H)]

color=1
cnt=0

for i in range(H):
    for j in range(W):
        if i%2==0:
            k=j
        else:
            k=-(1+j)
        
        ans[i][k]=color
        cnt+=1
        if cnt==A[color-1]:
            color+=1
            cnt=0


for i in range(H):
    print(*ans[i])