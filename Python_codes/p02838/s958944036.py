n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7
nisi = [0 for i in range(60)]
for i in range(n):
    for j in range(60):
        if (a[i] >> j) & 1 == 1:
            nisi[j] += 1
ans = 0
for i in range(60):
    ans += pow(2,i,mod)*nisi[i]*(n-nisi[i])%mod
ans %= mod
print(ans)