def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

n,k = map(int,input().split())

ans = 0

if k >= n-1:
    print(cmb(2*n-1,n,p))
else:

    for i in range(k+1):
        ###i:0人の部屋の数
        x = cmb(n,i,p)###0人の部屋の選び方
        y = cmb(n-1,i,p)
            ###0人でないn-i個の部屋にn人が入る時の人数の組み合わせ
            ###各部屋に1人以上入るので, それを上回る分についてのみ考える
            ###すなわち, n-(n-i)=i人についての組み合わせを考える
            ###人間i人, 仕切りn-i-1個
        ans += (x*y)%p
        ans %= p

    print(ans)


