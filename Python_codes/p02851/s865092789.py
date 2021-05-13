n,k=map(int,input().split())
a=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    a[i]+=a[i-1]
for i in range(1,n+1):
    a[i]=(a[i]-i)%k
b=[[] for i in range(n+1)]
for i in range(n+1):
    b[i]=[a[i],i]
b.sort()
left=0
right=0
ans=0
while left<n:
    while right<n:
        if b[left][0]==b[right+1][0] and b[right+1][1]-b[left][1]<k:
            right+=1
        else:
            break
    ans+=right-left
    left+=1
print(ans)