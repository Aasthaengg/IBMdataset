n,k = list(map(int,input().split()))
f = list(map(int,input().split()))

s = (10**9) // 2
step = s
best= 999999999999
import math

for j in range(50):
  c = 0
  arr = list(f)

  for i in range(n):
    if arr[i] > s:
      v = 0
      if arr[i] % s != 0:
        c += arr[i] // s
        v += arr[i] // s
      else:
        c += arr[i] // s
        v += arr[i] // s
        c -= 1
        v -= 1
      cor = 0
      if arr[i] % (v+1) != 0:
        cor = 1
      arr[i] = arr[i]//(v+1) + cor
    
  step = step//2
  step = max(1, step)
 
  if c<=k:
    best = min(best,max(arr))
   # print(s,best)
    s -= step
  else:
    s += step
    
  if s==0:
    s=1
      
print(best)