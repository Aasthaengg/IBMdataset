n = int(input())
a = []
b = []
for i in range(n):
  x, y = map(int, input().split())
  a.append(x)
  b.append(y)
ans = 0
a = a[::-1]
b = b[::-1]
for i in range(n):
  if (a[i] + ans) % b[i] == 0:
    next
  else:
    ans += b[i] - ((a[i]+ ans) % b[i])
print(ans)