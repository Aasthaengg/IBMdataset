H,W=map(int,input().split())
h,w=map(int,input().split())
white=H*W
black=h*W+w*H-h*w
print(white-black)