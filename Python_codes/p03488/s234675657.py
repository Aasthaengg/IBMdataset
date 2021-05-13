from collections import defaultdict as d
s=input()+"T"
x,y=map(int,input().split())
p=[[],[]]
c,e=0,0
for i in s:
    if i=="T":
        if e!=0:
            p[c].append(e)
            e=0
        c=(c+1)%2
    else:
        e+=1
def f(a,c,q):
    g=d(int)
    r=0
    if q!=0:
        if len(a)>0 and s[0]=="F":
            g[a[0]]=1
            r=1
        else:
            g[0]=1
    else:
        g[0]=1
    for j in a[r:]:
        t=d(int)
        for i,h in g.items():
            t[i-j]=1
            t[i+j]=1
        else:
            g=t
    return g[c]!=0
print("Yes" if f(p[0],x,1)*f(p[1],y,0)==1 else"No")