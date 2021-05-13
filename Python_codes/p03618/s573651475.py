# https://atcoder.jp/contests/agc019/tasks/agc019_b
from collections import defaultdict

A = input()
n = len(A)
cA = defaultdict(int)

for ch in A:
    cA[ch] += 1

all_num = 1 + n * (n - 1) // 2

for _, v in cA.items():
    all_num -= v * (v - 1) // 2

print(all_num)

