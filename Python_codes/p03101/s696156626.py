H, W =map(int,input().split())
h, w =map(int,input().split())

T = H*W
nu = h*W+H*w-w*h
print(T-nu)