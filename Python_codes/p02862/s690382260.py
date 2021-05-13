x, y = list(map(int, input().split(' ')))
# K馬(右上のみ) -> パスカルの三角形っぽい
mmm = 1000000000 + 7
sss = x + y
if sss % 3 != 0:
    print(0)
    exit()
hoge = sss // 3
# 上にp, 右にq
# 2p + q = y
# 2q + p = x
# p + q = hoge
# p = y - hoge
# q = x - hoge
p =  y - hoge
q = x - hoge
#print(hoge, p, q)
if p < 0 or q < 0:  # 3 0 の時で Wrong Answer
    print(0)
    exit()

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

init(hoge * 2 + 1)
print(choice(hoge, p) % mmm)

# nCk - TLE でした
# def choice(a, b):
#     if a == b or b == 0:
#         return 0
#     if a < b:
#         return choice(b, a)
#     bunshi = a
#     t = min(b, (a-b))
#     bunbo = t
#     for i in range(1, t):
#         bunshi *= (a-i) % mmm
#         bunbo *= (t-i) % mmm
#     return bunshi // bunbo
