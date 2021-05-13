n = int(input())
a = [int(x) for x in input().split()]

mi = 10 ** 7
ma = -(10 ** 7)
mi_idx = 0
ma_idx = 0
for i,v in enumerate(a):
  if v < mi:
    mi = v
    mi_idx = i
  if v > ma:
    ma = v
    ma_idx = i

print(2 * n - 1)
if abs(ma) >= abs(mi):
  for i in range(1, len(a) + 1):
    print(ma_idx + 1, i)
  for i in range(1, len(a)):
    print(i, i + 1)
else:
  for i in range(1, len(a) + 1):
    print(mi_idx + 1, i)
  for i in range(len(a), 1, -1):
    print(i, i - 1)
