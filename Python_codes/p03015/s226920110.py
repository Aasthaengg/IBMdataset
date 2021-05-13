MOD = 10**9+7

L = input()
N = len(L)

ans = 0
c = 0

for i in range(N):
    if L[i] == '1':
        ans += pow(3,N-i-1,MOD)*pow(2,c,MOD)
        ans %= MOD
        c += 1
        
ans += pow(2,c,MOD)
ans %= MOD

print(ans)
