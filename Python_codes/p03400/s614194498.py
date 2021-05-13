import math

n=int(input())
d,x=map(int,input().split())

ans=0
for i in range(n):
  num=int(input())
  ans+=math.ceil(d/num)
  
print(ans+x)