import sys
input = lambda: sys.stdin.readline().rstrip()

H,W = map(int,input().split())
h,w = map(int,input().split())

if H-h >0  and W-w > 0:
    print((H-h)*(W-w))
else:
    print(0)