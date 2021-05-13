# 組み合わせの総数 p=10**9+7 で割ったあまりを求める Satoooh Blog 2020/02/27 4分 
"""n<10**7 , p は素数"""
def cmb(n, r, p):

    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p



# 初期入力
import sys
input = sys.stdin.readline
N,K = (int(x) for x in input().split())

NN = 10 ** 4  # NN は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
p =10**9 +7
for i in range(2, NN + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

#青の場合の数
c_blue =[0]*(K+1)
b_blue =K
c_red =[0]*(K+1)
b_red = N -K
for i in range(1,K+1):
    gap_blue = i -1             #青の隙間＝赤を必ず置くべき場所
    c_blue[i] =cmb(b_blue -1 ,gap_blue ,p)
    b_red_free = b_red - gap_blue           #隙間に赤を置く⇒自由における赤が減る 
    #if b_red_free <0:
     #   continue
    c_red[i]  = cmb(gap_blue +2 +b_red_free -1 ,b_red_free ,p) 
    print(c_blue[i] *c_red[i] %p )