w,h,x,y=map(int,input().split())
a=w/2
b=h/2
s=w*h/2
cnt=0
if x==a and y==b:
    cnt=1
print(s,cnt)