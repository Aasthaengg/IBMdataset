W,H,x,y=list(map(int,input().split()))
s=W*H/2

d=0
if x==W/2 and y==H/2:
    d=1
print(s,d)