N = int(input())
a = list(map(int, input().split()))

ma = a[0]
mi = a[0]
maN = 0
miN = 0
for i in range(N):
  if a[i] > ma:
    ma = a[i]
    maN = i
  elif a[i] < mi:
    mi = a[i]
    miN = i

if abs(ma) > abs(mi):
  t = maN + 1
  f = 1
else:
  t = miN + 1
  f = -1

print(N * 2 - 1)
for i in range(1, N + 1):
  print(t, i)

if f == 1:
  for i in range(1, N):
    print(i, i + 1)
else:
  for i in range(N, 1, -1):
    print(i, i - 1)