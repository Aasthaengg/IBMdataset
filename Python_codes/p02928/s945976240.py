n,k = map(int,input().split())
a = list(map(int,input().split()))
MOD = 10**9+7

ans=0
for i in range(n):
    cnt1=0
    cntall=0
    for j in range(n):
        if a[i]>a[j]:
            cntall+=1
            if i<j:
                cnt1+=1

    ans =(ans + cnt1*k + cntall*k*(k-1)//2) % MOD

print(ans)
