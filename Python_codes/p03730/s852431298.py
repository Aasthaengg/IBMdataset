import sys
input = sys.stdin.readline

A, B, C = [int(x) for x in input().split()]

# Ax = By + C
# ⇄ Ax - By = C
# を満たすx, yが存在する
# CがGCD(A, B)の倍数であることが条件

# 最大公約数をユークリッドの互除法で求める
def GCD_by_euclid(x, y):
    if y == 0:
        return x
    else:
        return GCD_by_euclid(y, x % y)

gcd = GCD_by_euclid(A, B)
if C % gcd == 0:
    print("YES")
else:
    print("NO")