import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

W,H,x,y = MI()

# 長方形の中心

if 2*x == W and 2*y == H:
    print(H*W/2,1)
else:
    print(H*W/2,0)
