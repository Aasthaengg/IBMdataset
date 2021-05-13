nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]


N, P = map(int, input().split())  # 袋がN個, 2をPにしたい
A = list(map(lambda x: int(x)%2, input().split()))
# print(A)

kisuu = sum(A)  # 奇数個の袋の数
guusuu = N-kisuu  # 偶数個の袋の数

# Pが1のとき，偶数側の袋を任意の数と，奇数側の数を奇数個選ぶ
if P == 1:
    tmp_guusuu = 0
    tmp_kisuu = 0
    # 偶数側を任意の個数選ぶ
    for i in range(guusuu+1):
        tmp_guusuu += cmb(guusuu, i)
    for i in range(kisuu+1):
        if i % 2 == 0:
            continue
        tmp_kisuu += cmb(kisuu, i)
    print(tmp_guusuu*tmp_kisuu)

# Pが0のとき，偶数側の袋を任意の数と，奇数側の数を偶数個選ぶ
elif P == 0:
    tmp_guusuu = 0
    tmp_kisuu = 0
    # 偶数側を任意の個数選ぶ
    for i in range(guusuu+1):
        tmp_guusuu += cmb(guusuu, i)
    # 奇数側を0個数以上の偶数個選ぶ
    for i in range(kisuu+1):
        if i % 2 == 1:
            continue
        tmp_kisuu += cmb(kisuu, i)
    print(tmp_guusuu*tmp_kisuu)
