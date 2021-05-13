a,b,x=map(int,input().split())
l=(b-a+1)//x
w=(b-a+1)%x
if w==0:
    print(l)
else:
    p=0
    if a%x==0 or a%x+w>=x+1:
        p=1
    print(l+p)