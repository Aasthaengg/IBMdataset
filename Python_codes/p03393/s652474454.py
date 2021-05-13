S = input()

# 1 <= |S| <= 26
# lowercase

import sys
import copy

def next_permutation(a):
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break
    else:
        return False

    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

if len(S) == 26:
    sl = list(S)
    if next_permutation(sl):
        np = "".join(sl)
        for b in range(0, 26):
            if np[b] != S[b]:
                print(np[:b+1])
                exit()

    else:
        print(-1)
        exit()
else:
    hist = set(S)
    for c in range(0, 27):
        cand = chr(c+ord('a'))
        if cand not in hist:
            print(S+cand)
            sys.exit()