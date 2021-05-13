#!/usr/bin/env python3
n = int(input())
s = input()
INF = 10**9
white_cnt = s.count('.')
black_cnt = 0
ans = INF
for c in s:
    ans = min(ans, black_cnt + white_cnt)
    if c == '#':
        black_cnt += 1
    else:
        white_cnt -= 1
else:
    ans = min(ans, black_cnt + white_cnt)

print(ans)
