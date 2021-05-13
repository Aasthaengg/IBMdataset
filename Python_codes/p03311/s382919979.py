n=int(input())
a=list(map(int,input().split()))
for i in range(1,n+1):
    a[i-1]-=i
a.sort()
if n%2==1:
    ans=0
    b=a[n//2]
    for i in a:
        ans+=abs(i-b)
    print(ans)
else:
    ans1,ans2=0,0
    b1=a[n//2-1]
    b2=a[n//2]
    for i in a:
        ans1+=abs(i-b1)
        ans2+=abs(i-b2)
    print(min(ans1,ans2))