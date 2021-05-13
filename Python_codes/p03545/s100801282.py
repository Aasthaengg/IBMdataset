# -*- coding: utf-8 -*-
S = input()
space_cnt = 3
for i in range(2 ** space_cnt):
    ops = ["-"] * space_cnt
    for j in range(space_cnt):
        if (i >> j) & 1:
            ops[j] = "+"
    formula = ""
    for j in range(space_cnt):
        formula += S[j]+ops[j]
    formula += S[-1]
    if eval(formula)==7:
        break
print(formula+"=7")
