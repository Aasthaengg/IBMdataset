import math
n,d = map(int,input().split())
r = 0
for i in range(n):
  a,b = map(int,input().split())
  if d >= math.sqrt(a**2 + b**2):
  	r += 1
print(r)