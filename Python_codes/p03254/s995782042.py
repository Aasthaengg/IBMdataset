N, x = map(int, input().split())
a = [int(i) for i in input().split()]

res = 0
if x == sum(a):
  res = N
elif x > sum(a):
  res = N -1
else:
  a.sort()
  while x > 0:
    if x >= a[0]: res += 1
    x -= a.pop(0)

print(res)