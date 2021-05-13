n=int(input())
a=[]
b=[]

ans=0

for i in range(n):
  x,y=map(int,input().split())
  
  a.append(x)
  b.append(y)
  

for i in range(n):
  a[i]%=b[i]

a.reverse()
b.reverse()
  

for i in range(n):
  z=b[i]-(a[i]+ans)%b[i]
  if z==b[i]:
    z=0
  ans+=z


print(ans)