# -*- coding: utf-8 -*-

s = str(input())
n = len(s) - 1
answer = 0
for i in range(2 ** n):
    operation = [""] * n
    for j in range(n):
        if (i >> j) & 1:
            operation[n - 1 -j] = "+"
    
    formula = ""
    for p_n, p_o in zip(s, operation + [""]):
        formula += (p_n + p_o)
    
    answer += eval(formula)

print(answer)