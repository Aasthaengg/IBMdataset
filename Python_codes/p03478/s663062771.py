# -*- coding: utf-8 -*-

N, A, B = map(int, input().split())

ans = 0

for i in range(1, N+1):
    tmp_l = list(str(i))
    tmp_sum = 0
    for j in tmp_l:
        tmp_sum = tmp_sum + int(j)
    if A <= tmp_sum <= B:
        ans = ans + i

print(ans)