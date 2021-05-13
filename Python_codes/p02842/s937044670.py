import math
N = int(input())
flag = False
Min = math.floor(N / 1.08)
Max = math.floor( ( N + 1 ) / 1.08 + 1)
for i in range(Min, Max + 1):
  if math.floor( i * 1.08 ) == N:
    print( i )
    flag = True
    break
if not flag:
  print(':(')