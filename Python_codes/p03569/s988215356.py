#!/usr/bin/env python3
s = input()
n = len(s)
ans = 0
f = 0
b = -1
while True:
    if f - b > n - 1:
        break
    if s[f] != s[b]:
        if "x" in (s[f], s[b]):
            ans += 1
            f += "x" == s[f]
            b -= "x" == s[b]
        else:
            ans = -1
            break
    else:
        f += 1
        b -= 1
print(ans)
