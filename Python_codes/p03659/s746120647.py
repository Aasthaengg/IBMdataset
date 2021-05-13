n = int(input())
a = list(map(int, input().split()))

x = 0
y = sum(a)
ans = float("inf")
for i in range(n-1):
  x += a[i]
  y -= a[i]
  z  = abs(x-y)
  if z < ans: ans = z
print(ans)