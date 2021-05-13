# -*- coding: utf-8 -*-

s = input()
cnt = {l:0 for l in set(s)}
if len(cnt) != 2:
    print('No')
    exit(0)

for l in s:
    cnt[l] += 1
    if cnt[l] > 2:
        print('No')
        exit(0)

print('Yes')
