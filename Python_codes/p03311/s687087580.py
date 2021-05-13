n=int(input())
a=list(map(int,input().split()))
for i in range(n): a[i]-=i+1
a.sort()
if n%2==0: p=(a[n//2]+a[n//2-1])//2
else: p=a[n//2]
ans=0
for i in a: ans+=abs(i-p)
print(ans)