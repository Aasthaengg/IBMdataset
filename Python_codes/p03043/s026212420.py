n, k = map(int, input().split())

import math
ans = 0
for i in range(1,n+1):
  if i < k:
    t = math.log10(k/i)/math.log10(2)
    if t == int(t):
      ans += 1/(2**t)
    else:
      ans += 1/(2**(int(t+1)))
  else:
    ans += 1
  
print(ans/n)