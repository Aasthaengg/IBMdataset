import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
A,B,C = LI()
if A*B*C%2==0:
    print(0)
else:
    print(A*B*C//max(A,B,C))
