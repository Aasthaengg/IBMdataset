# 分母Bについて周期性があり、さらに単調増加のため、
# Nが周期以下ならN、Nが周期を超えるならB-1を代入した値が答え
a,b,n =map(int,input().split())
import math
x = min(n, b-1)
print((a * x) // b - a * (x // b))