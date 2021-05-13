import collections
n = int(input())
l = []
for i in range(n):
  l.append(int(input()))
d = collections.Counter(l)
ans = 0
for v in d.values():
  if v % 2 == 1:
    ans += 1
print(ans)