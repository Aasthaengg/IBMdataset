#66 A - Two Abbreviations
import math
N,M = map(int,input().split())
S = input()
T = input()

GCD = math.gcd(N,M)
L = N*M//GCD

dist_N = L//N
dist_M = L//M

# 同じ位置に書く文字は最大公約数 + 1 だけ存在する
for i in range(GCD):
    # S の s 文字目と T の t 文字目が同じ位置に来る
    s = dist_M * i
    t = dist_N * i
    if S[s] != T[t]:
        ans = -1
        break
else:
    ans = L
print(ans)