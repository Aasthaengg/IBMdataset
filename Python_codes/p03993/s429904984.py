n = int(input())
a = list(map(int, input().split()))

d = {}
ans = 0
for i in range(n):
  if a[i] in d and d[a[i]] == i+1: ans += 1
  else: d[i+1] = a[i]
print(ans)