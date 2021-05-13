from math import ceil,floor
N=int(input())
K=ceil(N/1.08)
if floor((K-1)*1.08)==N:
  print(K-1)
if floor(K*1.08)==N:
  print(K)
else:
  print(':(')