import numpy as np
n, k = [int(i) for i in input().split()]

A = []
check = np.ones(n)
for i in range(k):
  d = int(input())
  A = [int(i) for i in input().split()]
  for j in A:
    check[j-1] = 0
print(int(check.sum()))