#import numpy as np
n = int(input())
a = list(map(int,input().split()))
base = [0]*n
ans = 0

for i in range(n):
  if a[i] > n:
    ans += 1
  else:
    base[a[i]-1] += 1
    
for i in range(n):
  if base[i] == 0:
    continue
  elif base[i] == i+1:
    continue
  elif (base[i] < i+1) and (0 < base[i]):
    ans += base[i]
  elif i+1 < base[i]:
    ans += (base[i] - (i+1))
    
print(ans)