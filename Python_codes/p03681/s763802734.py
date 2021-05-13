import sys

mod = 10**9 + 7
n = 10**6
 
fact = [1]*(n+1)
rfact = [1]*(n+1)
r = 1
for i in range(1, n+1):
    fact[i] = r = r * i % mod
rfact[n] = r = pow(fact[n], mod-2, mod)
for i in range(n, 0, -1):
    rfact[i-1] = r = r * i % mod

#nPk (mod MOD) を求める
def perm(n, k):
    return fact[n] * rfact[n-k] % mod
 
# nCk (mod MOD) を求める
def comb(n, k):
    return fact[n] * rfact[k] * rfact[n-k] % mod

n, m = map(int,input().split())

if abs(n-m) > 1:
    print('0')
    sys.exit()

print(2*(perm(n,n)*perm(m,m))%mod) if n == m else print((perm(n,n)*perm(m,m))%mod)