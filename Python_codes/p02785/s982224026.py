import sys
n, k = map(int, input().split())
h = sorted(map(int, input().split()))
ans = 0

if k == 0:
  print(sum(h))
  sys.exit()

for i in h[:-k]:
  ans += i
print(ans)