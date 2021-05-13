# https://atcoder.jp/contests/arc061/tasks/arc061_a

from itertools import product

S = input()
l = len(S)

res = 0
for a in product(*[[0,1],]*(l-1)):
    c = 0
    st = S[0]
    for i, b in enumerate(a, start=1):
        if b == c:
            st += S[i]
        else:
            res += int(st)
            st = S[i]
        c = b
    res += int(st)

print(res)