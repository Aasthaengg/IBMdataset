from collections import Counter
n=int(input())
l=[]
for i in range(2,n+1):
    k=2
    t=i
    while k*k<=t:
        if t%k==0:
            l.append(k)
            t=t//k
        else:k+=1
    if n>0:l.append(t)

c=Counter(l)
ans=1
for key,value in c.items():
    ans*=value+1
print(ans%(10**9+7))

