#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
ans = 0
tmp_len = 0
for i in range(n):
    if a[i] == i + 1:
        tmp_len += 1
    else:
        ans += (1 + tmp_len) // 2
        tmp_len = 0
ans += (1 + tmp_len) // 2
print(ans)
