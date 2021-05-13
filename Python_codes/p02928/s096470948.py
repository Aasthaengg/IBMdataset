n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
mod = 10**9+7
ans = 0
for i in range(n):
    cnt = 0
    cnt2  =0
    for j in range(i):
        if a[i]>a[j]:
            cnt += 1
    for j in range(i+1,n):
        if a[i]>a[j]:
            cnt2+=1
    ans = (ans+cnt2*k*(k+1)//2+(cnt*k*(k-1)//2)%mod)%mod
print(ans)