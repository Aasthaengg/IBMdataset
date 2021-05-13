import math

n,m=map(int,input().split())
x=m*1800+n*100
ans=0
p=1

for i in range(1,10000):
  ans+=(x*i)*(p*(0.5**m))
  p-=p*(0.5**m)
  
ans=round(ans/100)

print(ans*100)