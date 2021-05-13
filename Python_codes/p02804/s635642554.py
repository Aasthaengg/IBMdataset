n, k = list(map(int, input().split(' ')))
aaa = sorted(list(map(int, input().split(' '))))
mmm = 1000000000 + 7
# 二項係数 mod [検索]
fac = []
inv = []
inv_fac = []
def init(n):
    fac.append(1)
    fac.append(1)
    inv.append(0)
    inv.append(1)
    inv_fac.append(1)
    inv_fac.append(1)
    for i in range(2, n):
        fac.append(fac[-1] * i % mmm)
        inv.append(mmm - inv[mmm%i] * (mmm // i) % mmm)
        inv_fac.append(inv_fac[-1] * inv[-1] % mmm)

def choice(a, b):
    if a < b:
        return 0
    return fac[a] * (inv_fac[b] * inv_fac[a-b] % mmm) % mmm
ans = 0
init(1000000)
for target in range(n):
    p_pattern = choice(target, k-1)
    #print(target, k-1, 'p_choice', choice(target, k-1))
    n_pattern = choice(n-target-1, k-1)
    #print(n-target-1, k-1, 'n_choice', choice(n-target-1, k-1))
    ans = (ans + aaa[target] * p_pattern - aaa[target] * n_pattern) % mmm
    #print(aaa[target], target-1, n-target, k-1, p_pattern, n_pattern)
print(ans % mmm)