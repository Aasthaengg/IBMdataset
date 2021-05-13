n=int(input());a=[];b=[2,1,0,0];x=0
for i in range(3):
  a.append(input())
for j in range(n):
  m=0
  if a[0][j]==a[1][j]:m+=1
  if a[1][j]==a[2][j]:m+=1
  if a[2][j]==a[0][j]:m+=1
  x+=b[m]
print(x)