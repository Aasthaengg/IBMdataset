mod = 10**9+7
def factrial(N):
    fc = [1, 1] + [None] * N
    inv = [0, 1] + [None] * N
    fcInv = [1, 1] + [None] * N
    for i in range(2, N+1):
        fc[i] = i*fc[i-1]%mod
        inv[i] = mod-(inv[mod%i]*(mod//i))%mod
        fcInv[i] = fcInv[i-1]*inv[i]%mod
    return fc, fcInv

def modCom(n, k):
    return 0 if n < k else fc[n] * fcInv[k] * fcInv[n-k] % mod

K = int(input())
S = input()
L = len(S)
fc, fcInv = factrial(L+K)
ans = 0
for i in range(K+1):
    ans += modCom(K-i+L-1, L-1) * pow(25, K-i, mod) * pow(26, i, mod)
    ans %= mod
print(ans)