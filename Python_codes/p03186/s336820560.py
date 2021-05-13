import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B,C = MI()
print(B+min(A+B+1,C))
