n, h, w = [ int(v) for v in input().split() ]
ans = 0
for i in range(n):
  a, b = [ int(v) for v in input().split() ]
  if a >= h and b >= w:
    ans += 1
print(ans)