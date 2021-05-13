N = int(input())

import math

ans = [0,0,0]

for h in range(1,3501):
  for n in range(h,3501):
    if (4*n*h-N*n-N*h) > 0:
      if (N*h*n)%(4*n*h-N*n-N*h) == 0 :
        ans = [h,n,(N*h*n)//(4*n*h-N*n-N*h)]
    if ans[0] != 0:
      break
  if ans[0] !=0:
    break

print(" ".join(map(str,ans)))