n=int(input())
a=sorted(map(int,input().split()))

cum=[0]*(n+1)
for i in range(n):
    cum[i+1]=cum[i]+a[i]
ans=1
for i in reversed(range(n-1)):
    if cum[i+1]*2<a[i+1]:
        break
    else:
        ans+=1
print(ans)