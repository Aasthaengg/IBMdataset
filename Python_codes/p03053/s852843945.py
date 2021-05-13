from collections import deque 
import sys
input = sys.stdin.readline
q = deque([])
h,w=map(int,input().split())
a=[list(input()) for i in range(h)]
x=[[-1,0],[1,0],[0,-1],[0,1]]
for i in range(h):
    for j in range(w):
        if a[i][j]=="#":
            for k in x:
                if 0<=i+k[0]<h and 0<=j+k[1]<w and a[i+k[0]][j+k[1]]==".":
                    a[i+k[0]][j+k[1]]="0"
                    q.append([i+k[0],j+k[1],1])
ans=0
while q:
    v=q.popleft()
    for k in x:
        if 0<=v[0]+k[0]<h and 0<=v[1]+k[1]<w and a[v[0]+k[0]][v[1]+k[1]]==".":
            a[v[0]+k[0]][v[1]+k[1]]="0"
            q.append((v[0]+k[0],v[1]+k[1],v[2]+1))
            ans=v[2]+1
print(ans)
