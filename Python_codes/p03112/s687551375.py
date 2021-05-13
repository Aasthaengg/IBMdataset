from bisect import bisect_left,bisect

icase=0
if icase==0:
    a,b,q=map(int,input().split())
    s=[0]*a
    for i in range(a):
        s[i]=int(input())
    t=[0]*b
    for i in range(b):
        t[i]=int(input())
    x=[0]*q
    for i in range(q):
        x[i]=int(input())
elif icase==1:
    a,b,q=2,3,4
    s=[100, 600]
    t=[400, 900, 1000]
    x=[150,2000,899,799]

si=[0]*a
j=-1
for i in range(a):
    si[i]=b-1
    while j+2<b:
        j+=1
        if abs(s[i]-t[j])<abs(s[i]-t[j+1]):
            si[i]=j
            j-=1
            break

ti=[0]*b
j=-1
for i in range(b):
    ti[i]=a-1
    while j+2<a:
        j+=1
        if abs(t[i]-s[j])<abs(t[i]-s[j+1]):
            ti[i]=j
            j-=1
            break
    
for k in range(q):
    sk=max(min(bisect(s,x[k])-1,a-1),0)
    tk=max(min(bisect(t,x[k])-1,b-1),0)
#    print(sk,tk)
    r1=abs(x[k]-s[sk])+abs(s[sk]-t[si[sk]])
    if sk+1<a:
        r2=abs(x[k]-s[sk+1])+abs(s[sk+1]-t[si[sk+1]])
    else:
        r2=r1
    r3=abs(x[k]-t[tk])+abs(t[tk]-s[ti[tk]])
    if tk+1<b:
        r4=abs(x[k]-t[tk+1])+abs(t[tk+1]-s[ti[tk+1]])
    else:
        r4=r3
#    print(min((r1,r2,r3,r4)),r1,r2,r3,r4)
    print(min((r1,r2,r3,r4)))
