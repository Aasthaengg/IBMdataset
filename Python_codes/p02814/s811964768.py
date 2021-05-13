# 最大公約数を返す
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
# 最小公倍数を返す
def lcm(a, b):
    return a * b // gcd(a, b)

N,M = map(int,input().split())
L = list(map(int,input().split()))

# ループを回しながら最小公倍数を計算していく
# 与えられたN個の偶数はすべて２で割っていく
leastCommonMultiple = L[0] // 2
for i in range(N):
    L[i] //= 2
    leastCommonMultiple = lcm(leastCommonMultiple, L[i])

# フラグ
c = 0

# Lに格納されているＮ個の数に含まれる素因数２の数が同じかどうかチェックする
while True:

    for i in range(N):
        # ２で割り切れない場合
        # L[i]に含まれている数すべてが２で割り切れないならＯＫ
        if L[i] % 2 == 1:
            c += 1
        # ２で割り切れるなら、２で割った数で上書き
        else:
            L[i] //= 2

    if not c == 0:
        break


if c == N:
    print( ((M // leastCommonMultiple) + 1) // 2 )
else:
    print(0)