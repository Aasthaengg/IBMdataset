import collections
n=int(input())
a=list(map(int,input().split()))

arr=collections.Counter(a)
ans=0
for i in arr:
    if i<=arr[i]:
        ans+=(arr[i]-i)
    else:
        ans+=arr[i]
print(ans)