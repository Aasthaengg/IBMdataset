n=int(input())
a=list(map(int,input().split()))

p=sum(a)

snuke=0
ans=10**10
for i in range(n-1):
    snuke+=a[i]
    ans=min(ans,abs(p-2*snuke))
print(ans)