w,h,n=map(int,input().split())
u,d,r,l=h,0,w,0
for _ in range(n):
    x,y,a=map(int,input().split())
    if a==1 and x>l: l=x
    if a==2 and x<r: r=x
    if a==3 and y>d: d=y
    if a==4 and y<u: u=y
if u>d and r>l: print((u-d)*(r-l))
else: print(0)