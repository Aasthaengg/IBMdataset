n,k=map(int,input().split())

l=sorted([int(input()) for _ in range(n)])

lst=[0]*(n-1)

temp=0
for i in range(n-1):
    temp=l[i+1]-l[i]
    lst[i]=temp

ll=[0]*(n)
temp=0
for ii in range(n-1):
    temp+=lst[ii]
    ll[ii+1]=temp

#print(lst)
#print(ll)
ans=10**9    
for j in range(n-k+1):
    ans=min(ans,ll[j+k-1]-ll[j])
print(ans)