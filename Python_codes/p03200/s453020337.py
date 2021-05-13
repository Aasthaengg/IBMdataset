#!/usr/local/bin/python3
# https://atcoder.jp/contests/agc029/tasks/agc029_a

S = list(input())
next_w = 0
ans = 0

for i in range(len(S)):
    if S[i] == 'W':
        back = i - next_w
        ans += back
        next_w = i - back + 1

print(ans)
