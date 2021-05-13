import collections
n = int(input())
b = [input() for _ in range(n)]
m = int(input())
r = [input() for _ in range(m)]
bc = collections.Counter(b)
rc = collections.Counter(r)
ans = 0
for x in bc.keys():
  ans = max(ans, bc[x]-rc[x])
print(ans)