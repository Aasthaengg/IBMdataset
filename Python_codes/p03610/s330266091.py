# -*- coding: utf-8 -*-

S = list(str(input()))

ans = []

for i in range(0, len(S), 2):
    ans.append(S[i])

print(*ans, sep='')