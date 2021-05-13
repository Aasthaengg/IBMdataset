# -*- coding: utf-8 -*-
S = input()
T = input()

ans = len(T)

for i in range(len(S) - len(T) + 1):
    diff = 0
    for t in range(len(T)):
        if T[t] != S[i + t]:
            diff += 1

    ans = min(ans, diff)

print(ans)