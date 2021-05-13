n,m=map(int,input().split())
a=[]
b=[]
c=[]
d=[]
x=[]
y=[]
l=[]
p=[]

for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)
    
for j in range(m):
    ci,di=map(int,input().split())
    c.append(ci)
    d.append(di)
    
for i in range(n):
    for j in range(m):
        x.append(abs(a[i]-c[j]))
        y.append(abs(b[i]-d[j]))
        l.append(x[j+i*m]+y[j+i*m])
    
    p.append(l.index(min(l))+1)   
    l=[]
    #x=[]
    #y=[]
    
for i in range(n):
    print(p[i])