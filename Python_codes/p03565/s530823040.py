# -*- coding: utf-8 -*-
S = input()
T = input()

candidates = []
for i in range(len(S) - len(T) + 1):
    is_ok = True
    for j in range(len(T)):
        if S[i+j] == '?' or S[i+j] == T[j]:
            pass
        else:
            is_ok = False

    # print(is_ok)
    if is_ok:
        candidate = S[:i] + T + S[i+len(T):]
        candidate = candidate.replace('?', 'a')
        candidates.append(candidate)

if candidates:
    candidates.sort()
    print(candidates[0])
else:
    print('UNRESTORABLE')