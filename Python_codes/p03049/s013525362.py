#!/usr/bin/env python3
n = int(input())
s = [input() for _ in range(n)]
tail_a = 0
head_b = 0
both_have = 0
ans = 0
for i in range(n):
    if s[i][0] == "B": head_b += 1
    if s[i][-1] =="A": tail_a += 1
    if s[i][0] == "B" and s[i][-1] =="A":
        both_have += 1
    ans += s[i].count("AB")
ans += min(tail_a,head_b)
if tail_a == head_b and tail_a == both_have:
    if both_have > 0:
        ans -= 1
print(ans)