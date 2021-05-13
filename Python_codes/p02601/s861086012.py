# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = float('inf')

A, B, C = list(map(int, input().split()))     # スペース区切り連続数字
K = int(input())    # 数字

r = 0
while A >= B:
    B *= 2
    r += 1

while B >= C:
    C *= 2
    r += 1

if r <= K:
    print("Yes")
else:
    print("No")
