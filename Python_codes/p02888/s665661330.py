n=int(input())
l=list(map(int,input().split()))
l.sort()
x=[0]*(10**3+1)
y=[]
for i in range(n):
    x[l[i]]+=1
for i in range(10**3+1):
    if i==0:
        y.append(0)
    else:
        y.append(y[i-1]+x[i])
y.append(y[len(y)-1])
ans=0
for i in range(n):
    for j in range(n):
        if i!=j:
            a=min(l[i],l[j])
            b=max(l[i],l[j])
            m=b-a
            M=min(a+b,10**3+1)
            g=y[M-1]-y[m]
            ans+=g
            if m<a<M:
                ans-=1
            if m<b<M:
                ans-=1
print(ans//6)