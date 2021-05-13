import sys

def S(): return sys.stdin.readline().rstrip()

N,L = map(int,S().split())

A = [L+i for i in range(N)]

if A[0] >= 0:
    print(sum(A)-A[0])
elif A[-1] <= 0:
    print(sum(A)-A[-1])
else:
    print(sum(A))