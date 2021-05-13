import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B,C = MI()
if A <= C <= B:
    print('Yes')
else:
    print('No')