# -*- coding: utf-8 -*-
s = input()
l = len(s)-1
ans = 0
ops = []

# +あり/なしの全探索のため、桁数-1の2乗
for i in range(2**l):
    op = [""] * l
    for j in range(l):
        if ((i >> j) & 1) == 1:
            op[l-1-j] = "+"
    ops.append(op)

for o in ops:
    str = [str for str in s]
    for k in range(len(o)):
        str.insert(2*k+1, o[k])
    ans += eval(''.join(str))

print(ans)
