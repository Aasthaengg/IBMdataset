import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


A,B = MI()
print((B+A-3)//(A-1))
