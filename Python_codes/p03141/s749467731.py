n = int(input())
a, b = [0]*n, [0]*n
for i in range(n):
  x, y = map(int, input().split())
  a[i], b[i] = x+y, y
ans = sum(sorted(a, reverse=True)[::2])-sum(b)
print(ans)