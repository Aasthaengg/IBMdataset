import math
n=int(input())
d,x=map(int,input().split())
for i in range(n):
  a=int(input())
  x+=(math.floor((d-1)/a))+1
print(x)