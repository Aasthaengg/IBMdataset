#!/usr/bin/env python3
s = input()
ans = [0] * len(s)
R = 0
L = 0
for i in range(len(s)):
    if s[i] == "R":
        R += 1
    else:
        ans[i] += R // 2
        ans[i - 1] += -(-R // 2)
        R = 0
    if s[-i - 1] == "L":
        L += 1
    else:
        ans[-i - 1] += L // 2
        ans[-i] += -(-L // 2)
        L = 0

print(*ans)
