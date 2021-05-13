#35 C - Anti-Division　
import math
A,B,C,D = map(int,input().split())

# C と D の最小公倍数の個数
lcm = C*D//math.gcd(C,D)
cnt_lcm = B//lcm - (A-1)//lcm

# C の倍数の個数
cnt_C = B//C - (A-1)//C 

# D の倍数の個数
cnt_D = B//D - (A-1)//D

# (範囲内の整数) - (C の倍数 + D の倍数 - C,D の公倍数)
ans = (B - A + 1) - (cnt_C + cnt_D - cnt_lcm)

# 範囲が 1 しかないとき
if A == B:
    # C でも D でも割り切れるとき
    if A%C == 0 and A%D == 0:
        print(0)
    else:
        print(1)
else:
    print(ans)