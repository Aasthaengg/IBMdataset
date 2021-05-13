n,k = map(int, input().split())
p = 10 ** 9 + 7

##逆元計算
N = n  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

fact = [ 0 for i in range(N+1)]
factinv = fact.copy()
inv = fact.copy()


fact[0], fact[1] = 1, 1
factinv[0], factinv[1] = 1, 1
inv[0], inv[1] = 0, 1
cmb_list = fact.copy()
cmb_list_sub1 = fact.copy()

for i in range(2, N + 1):
    fact[i] = (fact[i-1] * i) % p##階乗のリスト
    inv[i] = (-inv[p % i] * (p // i)) % p
    factinv[i] =(factinv[i-1] * inv[i]) % p##階乗の逆数のリスト
    
#nCrの0=< r <=n までの値のリストがほしい場合
for r in range(1,N+1):
    cmb_list[r] = fact[N] * factinv[r] * factinv[N-r] % p

for r in range(1, n):
    cmb_list_sub1[r] =fact[n-1]*factinv[r]*factinv[n-1-r]%p

ans = 0
if k <= n-1:
    for i in range(0,k+1):
        ans = (ans + cmb_list[i] * cmb_list_sub1[n-1-i])%p
else:
    for i in range(0,n):
        ans = (ans + cmb_list[i] * cmb_list_sub1[n-1-i])%p
print(ans)