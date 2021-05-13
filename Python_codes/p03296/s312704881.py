n=int(input())
a=list(map(int,input().split()))
ans=0
count=1
x=10000
for i in range(1,n):
    if a[i-1]==a[i]:
        count+=1
    else:
        ans+=count//2
        count=1
    if i==n-1:
        ans+=count//2
print(ans)
