n,k=map(int,input().split())
a=list(map(int,input().split()))
MOD=10**9+7
ans=0

part=0
all=0
for i in range(n):
    for j in range(i,n):
        if a[i]>a[j]:
            part+=1
    for l in range(n):
        if a[i]>a[l]:
            all+=1

ans=(k*part)%MOD+(all*(k*(k-1))//2)%MOD
print(ans%MOD)


