data = [[[0 for r in range(10)] for  f in range(3)] for b in range(4)]

n = int(input())
for nc in range(n):
  (b, f, r, v) = [int(i) for i in input().split()]
  data[b - 1][f - 1][r - 1] +=  v


for b in range(4):
  for f in range(3):
    for r in range(10):
      print(' {0}'.format(data[b][f][r]), end='')
    print()
  print('#' * 20) if b < 4 - 1 else print(end='')