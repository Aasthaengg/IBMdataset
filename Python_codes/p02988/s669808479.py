n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n) :
    if i==0 or i==n-1 : continue
    if a[i-1]>a[i] and a[i]>a[i+1] or a[i-1]<a[i] and a[i]<a[i+1] : ans+=1
print(ans)