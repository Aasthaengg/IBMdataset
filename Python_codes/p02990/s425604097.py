"""
Kをi分割する場合の数＝cmb(K+i-1,i-1)
両端が赤になる場合、両端が青になる場合、左端のみ赤になる場合、右端のみ赤になる場合についてそれぞれ計算すればよい。
"""
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

N,K = map(int,input().split())
for i in range(1,K+1):
    ans = 0
    #Kをi分割する場合の数
    divideK = cmb(K-i+i-1,i-1,p)
    #両端が赤の場合の置き方
    ans += divideK*cmb(N-K-(i+1)+i,i,p)%p
    ans %= p
    #両端が青の場合の置き方
    if i > 1:
        ans += divideK*cmb(N-K-(i-1)+i-2,i-2,p)%p
        ans %= p
    elif N-K == 0:
        ans += 1
    #左端のみが赤になる場合の置き方,右端のみが赤になる場合の置き方
    ans += divideK*cmb(N-K-i+i-1,i-1,p)*2%p
    ans %= p
    print(ans)