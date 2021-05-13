H,W=map(int,input().split())
h,w=map(int,input().split())
zentai=H*W
answer=zentai-(h*W+H*w-h*w)
print(answer)