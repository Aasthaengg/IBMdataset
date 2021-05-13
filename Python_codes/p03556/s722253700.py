from math import ceil, sqrt

N = int(input())
M = ceil(sqrt(N))
if M ** 2 <= N:
    print(M ** 2)
else:
    print((M - 1) ** 2)
