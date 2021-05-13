import numpy as np
MOD = 10**9 + 7
def solve(s):
    a = np.zeros(4, dtype=int)
    a[0] = 1
    for c in s:
        t = 2 * int(c == "?") + 1
        b = t * a % MOD
        if c == "A":
            b[1] += a[0]
        elif c == "B":
            b[2] += a[1]
        elif c == "C":
            b[3] += a[2]
        else:
            b[1:] += a[:-1]
        a = b
    return a[3] % MOD

s = input()
print(solve(s))