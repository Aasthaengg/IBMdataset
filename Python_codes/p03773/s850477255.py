import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B = MI()
print((A+B) % 24)
