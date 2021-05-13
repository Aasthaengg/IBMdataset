H,W = [int(i) for i in input().split()]
h,w = [int(i) for i in input().split()]
d = W * h + w * (H-h)
print(H*W-d)