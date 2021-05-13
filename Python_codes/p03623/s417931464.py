x,a,b=map(int,input().split())
y=abs(x-a)
z=abs(b-x)
if y<z:
    print('A')
else:
    print('B')