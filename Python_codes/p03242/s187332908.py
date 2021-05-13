#!/usr/bin/env python3

S = input()
ans = ''
for s in S:
    if s=='1': ans += '9'
    elif s=='9': ans += '1'
    else: ans += s
print(ans)

