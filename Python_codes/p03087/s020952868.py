import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,Q = MI()
S = LS2()
A = [0]*N

for i in range(1,N):
    if S[i-1] == 'A' and S[i] == 'C':
        A[i] = 1

from itertools import accumulate

A = list(accumulate(A))

for i in range(Q):
    l,r = MI()
    print(A[r-1]-A[l-1])
