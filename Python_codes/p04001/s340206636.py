#!/usr/bin/env python
# -*- coding: utf-8 -*-
S = input()
n = len(S) - 1
pattern = []
ans = 0

for i in range(2 ** n):
    tmp = [0] * n
    for j in range(n):
        if i >> j & 1:
            tmp[j] = "+"
    pattern.append(tmp)

for i in range(2 ** n):
    X = S[0]
    for j in range(n):
        if pattern[i][j] == "+":
            ans += int(X)
            X = S[j+1]
        else:
            X += S[j+1]
    ans += int(X)
print(ans)
