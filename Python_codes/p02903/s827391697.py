h,w,a,b=map(int,input().split())
c="1"*a+"0"*(w-a)
d="0"*a+"1"*(w-a)
for i in range(h):
    if i<b:
        print(c)
    else:
        print(d)