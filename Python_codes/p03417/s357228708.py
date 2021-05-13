import sys
input = sys.stdin.readline

H,W=list(map(int,input().split()))

num_ac = H*W
if H>=2 and W>=2:
    num_hd = 2*W+2*(H-2)
elif (H == 1 and W>= 2) or ( H>=2 and W==1):
    num_hd = 2

else:
    num_hd = 0

print(num_ac-num_hd)
