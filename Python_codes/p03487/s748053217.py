N = int(input())
a = list(map(int, input().split()))

d = {}
for ai in a:
  if ai in d:
    d[ai] += 1
  else:
    d[ai] = 1
  
ans = 0
for key in d:
  if d[key] >= key:
    ans += (d[key] - key)
  else:
    ans += d[key]
print(ans)
