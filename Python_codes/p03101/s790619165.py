H,W = [int(x) for x in input().split()]
h,w = [int(x) for x in input().split()]

print((H*W) - ((H*w) + (W*h)) + (h*w))