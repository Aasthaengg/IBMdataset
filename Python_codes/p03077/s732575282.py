from math import ceil
N=int(input())
A=[int(input()) for i in range(5)]
print(5+ceil(N/min(A)-1))
