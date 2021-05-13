k,n = map(int, input().split())

a= list(map(int,input().split()))
sa=[0]*n
for i in range(n-1):
    sa[i]=a[i+1]-a[i]
    sa[n-1]=a[0]+(k-a[n-1])
#print(sa)
ans=max(sa)
ans=k-ans
print(ans)