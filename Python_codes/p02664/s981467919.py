# -*- coding: utf-8 -*-
S = str(input());l = len(S);Str = ""
for num in range(l):
    if S[num] != "?":
        Str += S[num]
    else:
        Str += "D"
print(Str)