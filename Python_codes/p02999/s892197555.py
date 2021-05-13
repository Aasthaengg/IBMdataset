import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

X,A = MI()
print(0 if X < A else 10)
