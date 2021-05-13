import collections
n = int(input())
a = [int(input()) for i in range(n)]
ans = 0
a = collections.Counter(a)
for i in a.values():
  if i % 2 != 0:
    ans += 1
print(ans)

