H,W = (int(X) for X in input().split())
h,w = (int(X) for X in input().split())
print(H*W-h*W-w*H+h*w)