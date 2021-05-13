X, Y = map(int, input().split())
MOD = 10**9+7
MAX = 10**6+1

 # a!のテーブルfact
fact = [0] * MAX

def comb_init():
    # 累積積のイメージ
    fact[0] = fact[1] = 1
    for i in range(2, MAX):
        fact[i] = i * fact[i-1] % MOD

def comb(n, r):
    return fact[n]*pow(fact[r], -1, MOD)*pow(fact[n-r], -1, MOD)%MOD  

if (X+Y) % 3 != 0:
    print(0)
else:
    num = (X+Y)//3
    p = (Y - X + num) // 2
    q = (X + num - Y) // 2
    if not num >= min(p, q) >= 0:
        print(0)
        exit()
    comb_init()
    print(comb(num, min(p, q)))