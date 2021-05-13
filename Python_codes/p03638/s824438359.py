H,W=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

grid=[[0 for i in range(W)] for j in range(H)]
cur=0
curcnt=0
for i in range(H):
  for j in range(W):
    p=j
    if i%2==1:
      p=W-1-j
    grid[i][p]=cur+1
    curcnt+=1
    if curcnt==a[cur]:
      cur+=1
      curcnt=0
      
for i in range(H):
  print(*grid[i])