N=int(input())
x=[]
y=[]
l=[]
for i in range(N):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
l.sort()

d=dict()
r=[]
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        p = x[i]-x[j]
        q = y[i]-y[j]
        c=(p,q)
        if c in d:
            d[c]+=1
        else:
            d[c]=1
ans=0
#print(d)
for i,j in d.items():
    ans=max(ans,j)

print(N-ans)