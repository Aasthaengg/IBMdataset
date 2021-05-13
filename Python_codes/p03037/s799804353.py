n, m = map(int, input().split())
l = 1
r = 10**5
for _ in range(m):
  l_, r_ = map(int, input().split())
  l = max(l, l_)
  r = min(r, r_)
  
if r>=l:
  print(r-l+1)
else:
  print(0)