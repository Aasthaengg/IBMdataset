# -*- coding: utf-8 -*-
s = input()
l = len(s)-1
ans = 0
ops = []

# +あり/なしのbit全探索(桁数-1の2乗の範囲)
for i in range(1 << l):
    op = [''] * l
    for j in range(l):
        if ((i >> j) & 1) == 1:
            op[l-1-j] = '+'
    ops.append(op)

for op in ops:
    num = [digit for digit in s]
    for k in range(len(op)):
        # 演算子は奇数番目
        num.insert(2*k+1, op[k])
    ans += eval(''.join(num))

print(ans)
