#!/usr/bin/env python3
s = input()
n = len(s)
ans = 0
f = 0
b = -1
while True:
    if f - b > n - 1:
        break
    nf = s[f] in ("x", s[b])
    nb = s[b] in ("x", s[f])
    ans += "x" in (s[b], s[f]) and s[b] != s[f]
    if nf + nb < 1:
        ans = -1
        break
    f += nf
    b -= nb
print(ans)
