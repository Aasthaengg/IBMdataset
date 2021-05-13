from math import ceil
n=int(input())
d,x=map(int,input().split())
for i in range(n):
  s=int(input())
  x+=ceil(d/s)
print(x)