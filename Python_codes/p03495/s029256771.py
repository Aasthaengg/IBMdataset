import sys
from collections import Counter
N,K=map(int, sys.stdin.readline().split())
A=map(int, sys.stdin.readline().split())
C=Counter(A)
C=list(C.values())
C.sort()
print sum(C[:-1*K])