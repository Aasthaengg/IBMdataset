a,b=map(int,input().split())
x=a+b
if  x<a*2-1:
    print(a*2-1)
elif x<b*2-1:
    print(b*2-1)
else:
    print(x)