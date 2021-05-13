# -*- coding: utf-8 -*-
S = input()
result = 0
space_cnt = len(S)-1
for i in range(2 ** space_cnt):
    space = [""] * space_cnt
    for j in range(space_cnt):
        if ((i >> j) & 1):
            space[space_cnt -1 -j] = "+"
    formula = ""
    for i in range(space_cnt):
        formula += S[i]+space[i]
    formula += S[-1]
    result += eval(formula)
print(result)
