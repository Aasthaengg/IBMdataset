#!/usr/bin/env python3
s = input()
t = input()
ls = len(s)
lt = len(t)
ans = 1000  # min
for i in range(ls - lt + 1):
    tmp_cnt = 0
    for j in range(lt):
        if s[i + j] != t[j]:
            tmp_cnt += 1
    ans = min(ans, tmp_cnt)
print(ans)
