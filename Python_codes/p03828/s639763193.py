import math
n = int(input())
d = {}
       
for i in range(2,n+1):
  for j in range(2,i+1):
    while i%j == 0:
      i /= j
      if j in d:
        d[j] += 1
      else:
        d[j] = 2
ans = 1
for i in list(d.values()):
  ans *= i
print(ans%(10**9+7))