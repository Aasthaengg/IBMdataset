def s(p,q):
    a=p[0]
    b=p[1]
    c=q[0]
    d=q[1]
    return [(2*a+c)/3,(2*b+d)/3]
def t(p,q):
    a=p[0]
    b=p[1]
    c=q[0]
    d=q[1]    
    return [(a+2*c)/3,(b+2*d)/3]
def u(p,q):
    a=p[0]
    b=p[1]
    c=q[0]
    d=q[1]
    return [(a+c)/2+(3**(1/2))*(b-d)/6,(b+d)/2+(3**(1/2))*(c-a)/6]

def koch(p1,p2,n):
    if n==0:
        return [p1]
    else:
        return koch(p1,s(p1,p2),n-1)+koch(s(p1,p2),u(p1,p2),n-1)+koch(u(p1,p2),t(p1,p2),n-1)+koch(t(p1,p2),p2,n-1)

n=int(input())
a=[0,0]
b=[100,0]
for i in koch(a,b,n):
    print(str(i[0])+" "+str(i[1]))

print(str(b[0])+" "+str(b[1]))