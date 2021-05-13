a,b,c,d=map(int,input().split())
x=abs(c-a)
y=abs(d-b)
if a<c and b<=d:
    f=d+x
    e=c-y
    g=e-x
    h=f-y
elif a>=c and b<d:
    f=d-x
    e=c-y
    g=e+x
    h=f-y
elif a>c and b>=d:
    f=d-x
    e=c+y
    g=e+x
    h=f+y
else:
    f=d+x
    e=c+y
    g=e-x
    h=f+y
print(e,f,g,h)
