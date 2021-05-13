n,m=map(int,input().split())
a=[]
for x in range(m):
  s=list(map(int,input().split()))
  a.append(s)
  
min1=1
max1=n

for y in range(m):
  l=a[y][0]
  r=a[y][1]
  if min1<l:
    min1=l
  if max1>r:
    max1=r
    
if max1-min1>=0:
  print(max1-min1+1)
  
else:
  print(0)