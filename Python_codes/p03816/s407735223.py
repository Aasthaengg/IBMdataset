n=int(input())
a=[int(i) for i in input().split()]
ans=0
a.sort()
for i in range(1,len(a)):
    if(a[i]==a[i-1]):
        ans+=1
if(ans%2):
    print(n-(ans+1))
else:
    print(n-ans)
