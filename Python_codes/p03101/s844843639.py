H,W = map(int, input().split())
h,w = map(int, input().split())
sousuu = H*W
diff = h*W+w*(H-h)
print(sousuu-diff)