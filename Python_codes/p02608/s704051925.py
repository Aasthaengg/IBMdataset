n = int(input())
ans = [0 for _ in range(n+1)]

def f(x,y,z):
  return x**2+y**2+z**2+x*y+y*z+z*x
import math

for i in range(1, math.ceil(math.sqrt(n))):
  for j in range(i, math.ceil(math.sqrt(n))):
    for k in range(j, math.ceil(math.sqrt(n))):
      tmp = f(i, j, k)
      if tmp > n:
        break
      else:
        if i == j and j == k:
          ans[tmp] += 1
        elif i == j or j == k:
          ans[tmp] += 3
        else:
          ans[tmp] += 6
        
for i in range(1, n+1):
  print(ans[i])