n,q=map(int,input().split())
s=input()
l,r=[],[]
c=[0]*(n+1)
for i in range(q):
    a,b=map(int,input().split())
    l.append(a)
    r.append(b)
t=0
for i in range(n-1):
    if  s[i]=="A" and s[i+1]=="C":
        t+=1
    c[i+1]=t
c[n]=c[n-1]
c.append(c[n])
for i in range(q):
    print(c[r[i]-1]-c[l[i]-1])
