import collections

n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

cs = collections.Counter(s)
ct = collections.Counter(t)

ans = 0

for i, j in cs.items():
    ans = max(j-ct[i], ans)

print(ans)