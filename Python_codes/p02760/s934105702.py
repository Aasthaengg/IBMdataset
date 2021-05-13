a=[]
for _ in range(3):
  b=list(map(int,input().split()))
  a.append(b)
  
n=int(input())
for _ in range(n):
  x=int(input())
  for i in range(3):
    for j in range(3):
      if a[i][j]==x:
        a[i][j]=-1
        
if a[0][0]==a[0][1]==a[0][2] or a[1][0]==a[1][1]==a[1][2] or a[2][0]==a[2][1]==a[2][2] or a[0][0]==a[1][0]==a[2][0]  or a[0][1]==a[1][1]==a[2][1] or a[0][2]==a[1][2]==a[2][2] or a[0][0]==a[1][1]==a[2][2] or a[0][2]==a[1][1]==a[2][0]:
  print('Yes')
else:
  print('No')