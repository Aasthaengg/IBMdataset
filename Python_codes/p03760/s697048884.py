# -*- coding: utf-8 -*-

O = list(str(input()))
E = list(str(input()))

ans = ''

if len(O) - len(E) == 1:
    E.append('')

for i in range(len(O)):
    ans = ans + O[i] + E[i]

print(ans)