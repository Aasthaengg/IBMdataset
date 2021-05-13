# -*- coding: utf-8 -*-

S = input()

words = ['dream', 'dreamer', 'erase', 'eraser']

dp = [0] * 100010
dp[0] = 1
for i in range(len(S)):
    if dp[i]==0:
        continue
    for w in words:
        if S[i:i+len(w)] == w:
            dp[i+len(w)] = 1


if dp[len(S)] == 1:
    print('YES')
else:
    print('NO')
