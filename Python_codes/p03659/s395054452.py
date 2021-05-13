n = int(input())
a = list(map(int, input().split()))

s = sum(a)
t = 0
ans = float("inf")

for i in range(n-1):
  t += a[i]
  s -= a[i]
  ans = min(ans, abs(s-t))
print(ans)