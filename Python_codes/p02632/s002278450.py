g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
MOD = 10**9+7
for i in range(2, 2*10**6+1):
    g1.append((g1[-1] * i) % MOD)
    inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
    g2.append((g2[-1] * inverse[-1]) % MOD)

def comb(n, r, mod=MOD):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n-r] % mod

K = int(input())
S = input()
N = len(S)
NN = N + K
ans = 0
pow25 = [1]
pow26 = [1]
for i in range(K+1):
  pow25.append(pow25[-1]*25 % MOD)
  pow26.append(pow26[-1]*26 % MOD)

for i in range(K+1):
  n = NN - i
  ans = (ans + pow26[i]*pow25[n-N]*comb(n-1, N-1)) % MOD

print(ans)