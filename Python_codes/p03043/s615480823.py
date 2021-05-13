from math import log2,ceil

N,K=map(int,input().split())
SUM=0
for i in range(1,N+1):
  if i<K:
    n_trial = ceil(log2(K/i))
    tmp = 1/(2**n_trial)
  else:
    tmp = 1
  SUM += tmp
print(SUM/N)