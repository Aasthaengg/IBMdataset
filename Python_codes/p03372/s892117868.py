from itertools import accumulate
import bisect

n, c = [int(item) for item in input().split()]

xs, vs, xrs = [], [], []
for i in range(n):
  x, v = [int(item) for item in input().split()]
  xs.append(x)
  xrs.append(c-x)
  vs.append(v)
xrs = xrs[::-1]

lft_v = list(accumulate(vs))
rgt_v = list(accumulate(vs[::-1]))

lft_c = []
rgt_c = []
for i in range(n):
  lft_c.append(lft_v[i]-xs[i])
  rgt_c.append(rgt_v[i]-xrs[i])
  
lft_max = [0] * n
rgt_max = [0] * n
lm, rm = 0,0
for i in range(n):
  if lm < lft_c[i]:
    lm = lft_c[i]
  lft_max[i] = lm
  if rm < rgt_c[i]:
    rm = rgt_c[i]
  rgt_max[i] = rm

ans = 0
# No return
for i in range(n):
  ans = max(ans, lft_c[i], rgt_c[i])
  
# Includes return
for i in range(n-1):
  ans = max(ans, lft_c[i] - xs[i] + rgt_max[n-2-i])
  ans = max(ans, rgt_c[i] - xrs[i] + lft_max[n-2-i])
    
print(ans)