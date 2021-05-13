import math
N = int(input())
N_root = math.sqrt(N)
M = int(N_root)
list = []
for i in range(1,M+1):
  if N%i == 0:
    list.append(i+N//i-2)
list = sorted(list)
print(list[0])
