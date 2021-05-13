import numpy as np

N, K = map(int,input().split())

n_set = 0
if K % 2 == 0:
  if N >= K/2:
  	n_modhalf = (N - K/2) // K + 1
  	n_set += n_modhalf ** 3
  
n_modK = N // K
n_set += n_modK ** 3

print(int(n_set))