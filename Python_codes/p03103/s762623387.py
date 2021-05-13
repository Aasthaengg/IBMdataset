n, m = map(int, input().split())
lis = []
for i in range(n):
  lis.append(list(map(int, input().split())))
lis.sort()
ans = 0
for i, j in lis:
  ans += i * min(m, j)
  m -= min(m, j)
print(ans)