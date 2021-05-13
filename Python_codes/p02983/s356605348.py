import sys
l, r = map(int, input().split())
mod = 2019

if l%mod == 0 or r%mod == 0 or l//mod != r//mod:
  print(0)
  sys.exit()

ans = mod
for i in range(l, r):
  for j in range(i+1, r+1):
    ans = min(ans, i*j%mod)
print(ans)