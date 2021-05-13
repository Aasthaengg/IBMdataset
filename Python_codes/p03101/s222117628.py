H,W=map(int,input().split())
h,w=map(int,input().split())

if H*W==h*w:
    print(0)
else:
    print(H*W-(h*W+w*H-w*h))