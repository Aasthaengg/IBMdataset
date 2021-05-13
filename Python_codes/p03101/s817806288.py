H,W = map(int, input().split())
h,w = map(int, input().split())
S = H*W
s = W*h + w*(H-h)
print(S-s)
