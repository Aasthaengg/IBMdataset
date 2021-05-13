import sys

def S(): return sys.stdin.readline().rstrip()

A,B = map(int,S().split())

if A <= 9 and B <= 9:
    print(A*B)
else:
    print(-1)