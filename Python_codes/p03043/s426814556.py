from fractions import Fraction
import math

N, K = map(int, input().split())

p = Fraction(0, 1)
if K == 1:
    # 確定勝利
    print("1.0")
else:
    for i in range(1, N+1):
        # 出目i
        if i >= K:
            p += Fraction(1, N)
        else:
            n_win = math.ceil(math.log2(K / i))
            p += Fraction(1, 2**n_win * N)
    print(float(p))
