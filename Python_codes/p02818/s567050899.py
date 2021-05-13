import sys

def S(): return sys.stdin.readline().rstrip()

A,B,K = map(int,S().split())

if K <= A:
    print(A-K,B)
elif K >= A+B:
    print(0,0)
else:
    print(0,B-K+A)