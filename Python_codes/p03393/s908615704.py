from bisect import *

alpha = list(chr(c) for c in range(ord("a"), ord("z") + 1))

S = list(input())

not_used = list(set(alpha) - set(S))
not_used.sort()

if not not_used:
    can_use = []
    flag = False
    for i in range(len(S) - 1, -1, -1):
        # S[i]以上の値
        idx = bisect_left(can_use, S[i])
        if idx == len(can_use): # ない
            can_use.append(S[i])
        else: # ある
            S[i] = can_use[idx]
            idx = i
            flag = True
            break
    if flag:
        print(*S[:idx + 1], sep="")
    else:
        print(-1)
else:
    S.append(not_used[0])
    print(*S, sep="")