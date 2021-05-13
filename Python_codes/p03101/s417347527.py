H,W=map(int,input().split())
h,w=map(int,input().split())
Nall=H*W
Nblack=h*W + H*w
Noverlap=h*w
print(Nall-Nblack+Noverlap)