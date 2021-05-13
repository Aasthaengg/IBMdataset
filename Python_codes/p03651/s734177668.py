import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 全体のGCDを求める
all_gcd = A[0]
for m in A:
    all_gcd = math.gcd(all_gcd, m)

# Aの最大値より大きい数は作れない
# all_gcdの倍数でない数は作れない
if K <= max(A) and K % all_gcd == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
