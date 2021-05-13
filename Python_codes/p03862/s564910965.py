n,x=map(int,input().split())
a=list(map(int,input().split()))
sm=0
for i in range(n-1):
  b=max(a[i]+a[i+1]-x,0)
  a[i+1]=max(a[i+1]-b,0)
  sm+=b
 
print(sm)