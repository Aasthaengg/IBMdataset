n = int(input())
rootn = int(n**0.5) +1
ans = [0] * (n+1)
for x in range(1, rootn):
  for y in range(1, rootn):
    for z in range(1, rootn):
      cur = x**2 + y**2 + z**2 + x*y + y*z + z*x
      if cur <= n:
        ans[cur] += 1
print('\n'.join(map(str, ans[1:])))