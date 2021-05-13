n=int(input())
v=list(map(int,input().split()))
a=[0]*(10**5)
b=[0]*(10**5)
s,t=0,0
o,e,oi,ei=0,0,0,0
for i in range(1,n+1):
    if i%2==1:
        a[v[i-1]-1]+=1
        s+=1
    else:
        b[v[i-1]-1]+=1
        t+=1
o=max(a)
oi=[]
e=max(b)
ei=[]
for i in range(10**5):
    if a[i]==o:
        oi.append(i)
    if b[i]==e:
        ei.append(i)
if len(oi)==1 and len(ei)==1 and oi[0]==ei[0]:
    a.sort(reverse=True)
    b.sort(reverse=True)
    print(min(t-e+s-a[1],t-b[1]+s-o))
else:
    print(s+t-e-o)