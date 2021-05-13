N,M=map(int,input().split())

a=[]
b=[]
for i in range(N):
    a0,b0=map(int,input().split())
    a.append(a0)
    b.append(b0)

c=[]
d=[]
for i in range(M):
    c0,d0=map(int,input().split())
    c.append(c0)
    d.append(d0)

for i in range(N):
    l0=abs(a[i]-c[0])+abs(b[i]-d[0])
    ans=1
    for j in range(1,M):
        l=abs(a[i]-c[j])+abs(b[i]-d[j])
        if l0>l:
            l0=l
            ans=j+1
    
    print(ans)