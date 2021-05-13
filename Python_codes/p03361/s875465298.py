H,W=map(int,input().split())
p=[['.']*(W+2)]*(H+2)
for i in range(H):
  s=input()
  p[i+1]='.'+s+'.'
for i in range(1,H+1):
  for j in range(1,W+1):
    if p[i][j]=='#':
      flag=False
      for x,y in ([-1,0],[1,0],[0,-1],[0,1]):
        if p[i+x][j+y]=='#':
          flag=True
          break
      if not flag:
        print('No')
        exit()
print('Yes')