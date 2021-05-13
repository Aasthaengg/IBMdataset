# D - Patisserie ABC
n,m=map(int,input().split())
x,y,z=[],[],[]
for i in range(n):
    xx,yy,zz=map(int,input().split())
    x.append(xx)
    y.append(yy)
    z.append(zz)

o=[]
for i in range(2**3):
    op = [0]*3
    for j in range(3):
        if ((i>>j)&1):
            op[3-1-j]=1
    o.append(op)
ans=0
for oo in o:
    l=[]
    for i in range(n):
        t=0
        if oo[0]:t+=x[i]
        else:t-=x[i]
        if oo[1]:t+=y[i]
        else:t-=y[i]
        if oo[2]:t+=z[i]
        else:t-=z[i]
        l.append(t)
    l.sort()
    ans=max(abs(sum(l[:m])),abs(sum(l[n-m:])),ans)
print(ans)