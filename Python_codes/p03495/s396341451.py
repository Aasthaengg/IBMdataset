n,k=map(int,input().split())
a=list(map(int,input().split()))
sa=set(a)
nums=len(sa)
if nums<=k:
    print(0)
else:
    num=[0]*n
    for i in range(n):
        num[a[i]-1]+=1
    num.sort()
    ans=0
    for i in range(n-k):
        ans+=num[i]
    print(ans)
