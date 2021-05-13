A,B,C,K=map(int,input().split())
import numpy as np
X = np.array([A,B,C])
Y = np.array([1,-1,0])
M = np.matrix('0 1 1; 1 0 1; 1 1 0')

def pow_V(Z,n):
  bin_n = format(n, 'b')
  ans = np.matrix('1 0 0; 0 1 0; 0 0 1')
  for i in range(0,len(bin_n)):
    if i == 0:
      XX = Z
    else:
      XX = XX * XX
    if bin_n[-(i+1)]=='1':
      ans = ans * XX
  return ans
MK = pow_V(M,K)
R = np.inner(Y, (X * MK))[0,0]
print(R)