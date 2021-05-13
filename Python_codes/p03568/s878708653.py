import numpy as np
N = int(input())
A = list(map(int, input().split()))
count=1
for i in range(N):
  if A[i]%2==0:
    count*=2

print(3**N-count)