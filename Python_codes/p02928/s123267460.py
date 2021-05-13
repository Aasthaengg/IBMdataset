#https://scrapbox.io/pocala-kyopro/B_-_Kleene_Inversion
MOD = 1000000007
N,K = map(int,input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    migi = 0
    zentai = 0
    for j in range(i,N):
        if A[i] > A[j]:
            migi += 1
    for j in range(N):
        if A[i] > A[j]:
            zentai += 1
            
    ans += migi * K % MOD
    ans %= MOD
    ans += (K-1)*K//2 % MOD * zentai % MOD
    ans %= MOD
print(ans)
