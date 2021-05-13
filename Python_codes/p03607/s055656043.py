n = int(input())
d = {}
for _ in range(n):
  a = int(input())
  if a in d: d[a] += 1
  else: d[a] = 1

ans = 0
for i in d.values():
  if i%2 != 0: ans += 1
print(ans)