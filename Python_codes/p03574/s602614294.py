n,m=map(int,input().split())
r=[[*input()] for _ in range(n)]
ans=[[[0] for _ in range(m)] for _ in range(n)]
dir=[[0,0,1,1,1,-1,-1,-1],[-1,1,-1,0,1,-1,0,1]]
for i in range(n):
  for j in range(m):
    count=0
    if r[i][j]=='#':
      ans[i][j]='#'
      continue
    for k in range(8):
      dx,dy=i+dir[0][k],j+dir[1][k]
      if 0<=dx<n and 0<=dy<m and r[dx][dy]=='#':
        count+=1
    ans[i][j]=count
[print(*i,sep='') for i in ans]