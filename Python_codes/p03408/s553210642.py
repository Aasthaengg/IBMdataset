import collections
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

sc = collections.Counter(s)
tc = collections.Counter(t)
ans = 0
for x in sc.keys():
  ans = max(ans,sc[x]-tc[x])
print(ans)