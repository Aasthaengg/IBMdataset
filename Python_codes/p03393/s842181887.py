import sys

S = sys.stdin.readline().strip()
ls = len(S)

if ls == 26 and list(S) == sorted(S, reverse=True):
    print(-1)
    sys.exit()

alpha = "abcdefghijklmnopqrstuvwxyz"
exists = set(S)
if ls < 26:
    for a in alpha:
        if a not in exists:
            print(S + a)
            sys.exit()
else:
    for i in range(ls):
        tmp = S[ls-1-i:] 
        if list(tmp) != sorted(tmp, reverse=True):
            break
    remain = []
    exists = set(S[:ls-i-1])
    last = S[ls-i-1]
    for a in alpha:
        if a not in exists:
            remain.append(a)

    for r in sorted(remain, reverse=True):
        if last < r:
            min_a = r
    # min_a = sorted(remain)[0]
    print(S[:ls-i-1] + min_a)