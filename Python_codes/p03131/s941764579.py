k, a, b = map(int, input().split())
n = 1
m = 0
n += a - 1
k -= a - 1
if a + 1 < b:
  n += (b - a) * (k // 2) + k % 2
else:
  n += k
print(n)
