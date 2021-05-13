import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B,C = MI()
print('Yes' if A <= C <= B else 'No')
