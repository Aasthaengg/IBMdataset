n,k=map(int,input().split())
a=sorted([list(map(int,input().split()))for i in range(n)],key=lambda x:-x[1])
t=[0]*(n+1)
p,q=0,0
for i in a[:k]:
    p+=i[1]
    if t[i[0]]==0:
        q+=1
    t[i[0]]+=1
s=0
d=p+q*q
c=a[:k][::-1]
for i in a[k:]:
    if t[i[0]]==0:
        while s!=k:
            if t[c[s][0]]==1:
                s+=1
            else:
                break
        if s==k:
            break
        else:
            t[i[0]]+=1
            p-=c[s][1]-i[1]
            q+=1
            d=max(d,p+q*q)
            s+=1
print(d)