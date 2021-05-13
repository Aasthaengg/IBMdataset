def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    
    if temp!=1:
        arr.append([temp, 1])
    
    if arr==[]:
        arr.append([n, 1])
    
    return arr

g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
MOD = 10**9+7
for i in range(2, 2*10**5):
    g1.append((g1[-1] * i) % MOD)
    inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
    g2.append((g2[-1] * inverse[-1]) % MOD)

def memo_comb(n, r, mod=MOD):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n-r] % mod


N, M = map(int, input().split())
if M == 1:
  print(1)
  quit()

n = N - 1
fac_m = factorization(M)
ans = 1
for _, m in fac_m:
  ans *= memo_comb(m+n, n)
  ans %= MOD

print(ans)