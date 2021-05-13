x = list(map(int, input().split()))
tmp = 0
for i in range(0, 10):
  if tmp == 0:
    tmp = x[2]
  tmp = x[0] * tmp - x[1]
  print(tmp)