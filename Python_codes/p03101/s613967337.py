H,W=map(int,input().split())
h,w=map(int,input().split())
all=H*W
black=W*h+H*w
double=h*w
print(int(all)-int(black)+int(double))
