n,m=map(int,input().split())
h=list(map(int,input().split()))
a,b=[],[]
for i in range(m):
    c,d=map(int,input().split())
    a.append(c)
    b.append(d)
s=[]
for i in range(m):
    if h[a[i]-1]<h[b[i]-1]:
        s.append(a[i])
    elif h[a[i]-1]>h[b[i]-1]:
        s.append(b[i])
    else:
        s.append(a[i])
        s.append(b[i])
d=len(set(s))
print(n-d)