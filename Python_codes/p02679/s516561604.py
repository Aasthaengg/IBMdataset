# E - ∙ (Bullet)
import sys
from collections import defaultdict

readline = sys.stdin.readline
MOD = 1000000007
N = int(readline())

# イワシの傾きをA/Bとする。
# A/Bは予めgcdで割って約分し、同じ傾きのものを揃えておく。
# このとき、仲の悪い組合せは(A, B)に対して(B, -A)となるもの。 
# 前者をS、後者をTとして考える。
d_S = defaultdict(int)
d_T = defaultdict(int)

def gcd(x, y):
    if x == 0:
        return y
    else:
        return gcd(y%x, x)

pow2_mod = [1] + [0] * (N * 2)
for i in range(1, N * 2):
    pow2_mod[i] = pow2_mod[i-1] * 2 % MOD

zeros = 0
for i in range(N):
    A, B = map(int, readline().split())
    # (0, 0)のイワシは他の全てのイワシと仲が悪いため、
    # 1匹のみでしか選ぶことができない。最後にこの数を足す。
    if A == 0 and B == 0:
        zeros += 1
    # (?, 0),(0, ?)のイワシは、?がどのような数字であろうとも
    # この組合せであれば仲が悪い。一律、(1,0)(0,-1)として考える。
    elif A == 0:
        d_S[(1, 0)] += 0
        d_T[(0, -1)] += 1
    elif B == 0:
        d_S[(1, 0)] += 1
        d_T[(0, -1)] += 0
    else:
        g = gcd(A, B)
        A //= g
        B //= g
        # いずれもマイナスの場合、傾きはプラスになる
        if A < 0 and B < 0:
            A *= -1
            B *= -1
        if A * B > 0:
            d_S[(A, B)] += 1
            d_T[(B, -A)] += 0
        # 片方がマイナスの場合、必ずAがマイナスになるよう揃える
        else:
            if A > B:
                A, B = B, A
            d_S[(-A, B)] += 0
            d_T[(B, A)] += 1

ans = 1
for (si, sj), s_cnt in d_S.items():
    t_cnt = d_T[(sj, -1*si)]
    tmp = 0
    tmp += pow2_mod[s_cnt] - 1 # Sから1匹以上選ぶ組合せ
    tmp += pow2_mod[t_cnt] - 1 # Tから1匹以上選ぶ組合せ
    tmp += 1 # どちらも選ばない組合せ
    ans = (ans * tmp)%MOD

ans -= 1 # 最終的に1匹も選ばない組合せ
ans += zeros # (0, 0)のイワシの数

print(ans%MOD)