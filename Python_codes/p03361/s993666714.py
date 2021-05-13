h,w=map(int,input().split())
lst=[]
lst.append('.'*(w+2))
for i in range(h):
  lst.append('.'+input()+'.')
lst.append('.'*(w+2))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(1,h+1):
  for j in range(1,w+1):
    if lst[i][j]=='#':
      judge=False
      for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        if lst[nx][ny]=='#':
          judge=True
          
      if judge==False:
        print('No')
        exit()
        
print('Yes')