import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

X,t = MI()
print(max(0,X-t))
