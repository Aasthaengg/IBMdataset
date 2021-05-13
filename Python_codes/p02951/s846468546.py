x,y,z=map(int,input().split())
s=x-y
if(s>z):
    print(0)
else:
    print(z-s)