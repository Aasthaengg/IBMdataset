from bisect import *
N, L = map(int, input().split())
A = list(range(L,L+N))
res = sum(A)
print(res - A[min(bisect_left(A,0),len(A)-1)])