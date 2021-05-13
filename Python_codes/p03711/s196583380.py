n = 12
data = [0 for i in range(n + 1)]
data[1] = 1
data[3] = 1
data[5] = 1
data[7] = 1
data[8] = 1
data[10] = 1
data[12] = 1
data[4] = 2
data[6] = 2
data[9] = 2
data[11] = 2
data[2] = 3
a, b = map(int,input().split())
if data[a] == data[b]:
  print('Yes')
else:
  print('No')