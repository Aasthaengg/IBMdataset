#!/usr/bin/env python3
n, m = map(int, input().split())
ans = []
i = 1
while i < m + 2 - i:
    ans.append([i, m + 2 - i])
    i += 1
i = m + 2
while i < 3 * m + 3 - i:
    ans.append([i, 3 * m + 3 - i])
    i += 1
for i in ans:
    print(*i)
