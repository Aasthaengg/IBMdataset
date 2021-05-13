# coding: utf-8
# Your code here!
import sys

sys.setrecursionlimit(10**9)

def dfs(h,w,start):
    if S[h][w]=="#":
        black[start[0]][start[1]]+=1
    else:
        white[start[0]][start[1]]+=1
    
    visited[h][w]=1
    if h!=0:
        if visited[h-1][w]==-1 and S[h-1][w]!=S[h][w]:
            dfs(h-1,w,start)
    if w!=0:
        if visited[h][w-1]==-1 and S[h][w-1]!=S[h][w]:
            dfs(h,w-1,start)        
    if h!=H-1:
        if visited[h+1][w]==-1 and S[h+1][w]!=S[h][w]:
            dfs(h+1,w,start)        
    if w!=W-1:
        if visited[h][w+1]==-1 and S[h][w+1]!=S[h][w]:
            dfs(h,w+1,start)    
    return 

H,W=map(int,input().split())

S=[]

for _ in range(H):
    S.append(list(input()))

visited=[[-1 for j in range(W)] for i in range(H)]
black=[[0 for j in range(W)] for i in range(H)]
white=[[0 for j in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        if visited[i][j]==-1:
            dfs(i,j,[i,j])
        #print(visited)

ans=0
for i in range(H):
    for j in range(W):
        ans+=black[i][j]*white[i][j]
"""
print(S)
print(black)
print(white)
"""
print(ans)