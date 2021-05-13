n,m,k=map(int,input().split())
board=[list(input()) for _ in range(n)]
cnt=[0]*n
for i in range(n):
  tmp=0
  for j in range(m):
    if board[i][j]=='#':
      tmp+=1
  cnt[i]=tmp
ans=[[0]*m for _ in range(n)]
num=1
for i in range(n):
  if cnt[i]==0:
    continue
  tmp=0
  for j in range(m):
    ans[i][j]=num
    if board[i][j]=='#':
      tmp+=1
      if tmp>=2:
        ans[i][j]+=1
        num+=1
  num+=1
for i in range(1,n):
  if cnt[i]==0:
    for j in range(m):
      ans[i][j]=ans[i-1][j]
for i in range(n-2,-1,-1):
  if cnt[i]==0:
    for j in range(m):
      ans[i][j]=ans[i+1][j]
for i in range(n):
  print(*ans[i])