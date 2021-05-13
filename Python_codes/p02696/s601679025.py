import math

A, B, N = map(int, input().split())

if N >= B-1:  # x = B-1のときに最大値
    beta = (B-1)/B
    print(math.floor(A * beta))

else:
    beta = N/B
    print(math.floor(A * beta))
