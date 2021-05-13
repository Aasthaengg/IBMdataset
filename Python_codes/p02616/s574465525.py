n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
n=len(arr)
l=0
r=n-1
ans=1
if k%2==1:
    ans=arr[0]
    l=1
m=10**9+7
if ans<0:
    ans=1
    for i in range(k):
        ans*=arr[i]
        ans%=m
    print(ans)
    quit()
for i in range(k//2):
    po=arr[l]*arr[l+1]
    ne=arr[r]*arr[r-1]
    if po>=ne:
        l+=2
        ans*=po
        ans%=m
    else:
        r-=2
        ans*=ne
        ans%=m
print(ans)

