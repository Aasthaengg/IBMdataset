n, m = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(m)]
l = []
r = []
for i in range(m):
  l.append(lr[i][0])
  r.append(lr[i][1])
lm = max(l)
rm = min(r)
ans = 0
for i in range(1, n+1):
  if lm <= i <= rm:
    ans += 1
print(ans)