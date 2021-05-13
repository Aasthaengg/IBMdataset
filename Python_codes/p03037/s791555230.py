import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,M = MI()
A = [0]*(N+2)

for i in range(M):
    l,r = MI()
    A[l] += 1
    A[r+1] -= 1

from itertools import accumulate

A = list(accumulate(A))
print(sum(A[i] == M for i in range(1,N+1)))
