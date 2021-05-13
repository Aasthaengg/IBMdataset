n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
  x,y=map(int,input().split())
  a.append([x,y])
for i in range(m):
  x,y=map(int,input().split())
  b.append([x,y])
for i in a:
  ans=10**18
  t=0
  for j in range(m):
    if abs(i[0]-b[j][0])+abs(i[1]-b[j][1])<ans:
      t=j+1
      ans=abs(i[0]-b[j][0])+abs(i[1]-b[j][1])
  print(t)
