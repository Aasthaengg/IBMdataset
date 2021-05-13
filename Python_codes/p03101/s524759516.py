H,W = map(int,input().split())
h,w = map(int,input().split())
all = H*W
paint =h*W + w*H - h*w
print(all - paint)