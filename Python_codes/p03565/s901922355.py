# -*- coding: utf-8 -*-
S = input()
T = input()
candidates = list()
for i in range(len(S) - len(T) + 1):
    flag = True
    for j in range(len(T)):
        if S[i+j] != T[j] and S[i+j] != "?":
            flag = False
            break
    if flag:
        s = S[:i] + T + S[i+j+1:]
        candidates.append(s.replace("?", "a"))
if candidates:
    candidates.sort()
    print(candidates[0])
else:
    print("UNRESTORABLE")
