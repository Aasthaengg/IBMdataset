from math import ceil
N = int(input())
L = [int(input()) for k in range(5)]
print(4+ceil(N/min(L)))
