h,w=map(int,input().split())
maze=[]
lst=['.']*(w+2)
maze.append(lst)

for i in range(h):
  lst2=list(input())
  lst2=['.']+lst2+['.']
  maze.append(lst2)

maze.append(lst)


ans=[[None]*w for i in range(h)]

dx=[1,1,1,-1,-1,-1,0,0]
dy=[1,0,-1,1,-1,0,1,-1]

for i in range(1,h+1):
  for j in range(1,w+1):
    cnt=0
    if maze[i][j]=='#':
      ans[i-1][j-1]='#'
      continue

    for k in range(8):
      s=i+dx[k]
      t=j+dy[k]
      if maze[s][t]=='#':
        cnt+=1
    ans[i-1][j-1]=str(cnt)
    
for i in range(h):
  answer=''
  for j in range(w):
    answer+=ans[i][j]
  
  print(answer)