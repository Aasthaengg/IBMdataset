import collections
n = int(input())
a = list(map(int, input().split()))
d = {}
ans = 0
for i in range(n):
  d[i + 1] = a[i]
for i in range(n):
  if d[d[i + 1]] == i + 1:
    ans += 1
ans //= 2
print(ans)