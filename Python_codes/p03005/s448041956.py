import numpy as np

a = input().split(" ")
N = int(a[0])
K = int(a[1])

if K == 1:
    print(0)
else:
    print(N-K)