n = int(input())
b = [input() for _ in range(n)]
m = int(input())
r = [input() for _ in range(m)]
c = list(set(b+r))
ans = 0
for i in range(len(c)):
  d = b.count(c[i])-r.count(c[i])
  ans = max(0, ans, d)
print(ans)