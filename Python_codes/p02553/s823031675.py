a,b,c,d=map(int,input().split())
x=max(a*c,a*d,b*c,b*d)
if (b<0 and 0<c) or (d<0 and 0<a):
    print(x)
else:
    print(max(x,0))
