import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B = MI()

if A == B:
    print(A+B)
else:
    print(max(A,B)*2-1)