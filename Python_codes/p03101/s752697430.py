import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

H,W = MI()
h,w = MI()
print((H-h)*(W-w))