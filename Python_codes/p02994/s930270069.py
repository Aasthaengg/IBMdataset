n, l = map(int, input().split())
s = (l + l + n - 1) * n // 2
Ps = [l] * n
for i in range(n):
  Ps[i] += i
if 0 in Ps:
  print(s)
elif Ps[n - 1] < 0:
  print(s - Ps[n - 1])
else:
  print(s - Ps[0])