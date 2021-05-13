import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B,C = MI()
if A == B:
    print(C)
if B == C:
    print(A)
if C == A:
    print(B)