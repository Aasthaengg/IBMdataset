n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
x,y = a[0][0],a[0][1]
for i in range(1,n):
  xr=(x+a[i][0]-1)//a[i][0]
  yr=(y+a[i][1]-1)//a[i][1]
  r=max(xr,yr)
  x=r*a[i][0]
  y=r*a[i][1]
print(x+y)