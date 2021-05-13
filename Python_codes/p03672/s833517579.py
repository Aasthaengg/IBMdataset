#!/usr/bin/env python3

S = input()[:-1]

if len(S) < 2:
    ans = 0

for i in range(1,len(S) // 2+1):
    if S[0:i] == S[i:i*2]:
        ans = i * 2

print(ans)

