n = int(input())
f = [0]*n
for i in range(n):
  f[i] = [int(x) for x in input().split()]

p = [0]*n
for i in range(n):
  p[i] = [int(x) for x in input().split()]

ans = -10**9-7

for i in range(2**10):
  o = [0]*10
  for j in range(10):
    if (i >> j) & 1:
      o[j] = 1
  if not any(o):
    continue
  sub = 0
  for k in range(n):
    key = 0
    for j in range(10):
      if o[j] and f[k][j]:
        key += 1
    sub += p[k][key]
  if sub > ans:
    ans = sub

print(ans)