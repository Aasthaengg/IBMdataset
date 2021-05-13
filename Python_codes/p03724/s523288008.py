n,m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
s = [0] * (10 ** 5+1)
for a,b in ab:
  s[a] += 1
  s[b] += 1
if any([i % 2 for i in s]):
  print("NO")
else:
  print("YES")