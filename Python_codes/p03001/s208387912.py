w,h,x,y=map(int,input().split())
ma=w*h/2
W=w//2
H=h//2
if w%2==0 and h%2==0 and W==x and H==y:
    boo=1
else:
    boo=0

print(ma,boo)