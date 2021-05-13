import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B,C,D = MI()
print(max(A*B,C*D))