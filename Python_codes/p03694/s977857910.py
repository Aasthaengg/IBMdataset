_=int(input())
a=list(set(map(int,input().split())))
a.sort(reverse=True)
ans=0
for i in range(len(a)-1):
    ans+=a[i]-a[i+1]
print(ans)