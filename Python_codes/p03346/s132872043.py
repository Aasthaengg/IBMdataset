# -*- coding: utf-8 -*-
from sys import stdin

s_in = lambda: stdin.readline()[:-1]  # s = s_in()
d_in = lambda: int(stdin.readline())  # N = d_in()
ds_in = lambda: list(map(int, stdin.readline().split()))  # List = ds_in()


N = d_in()

aranged_list = [0] * N
for i in range(N):
    idx = d_in()
    aranged_list[idx-1] = i

ans, count = 0, 0
temp = -1
for i in aranged_list:
    if i > temp:
        count += 1
        temp = i
    else:
        ans = max(ans, count)
        count = 1
        temp = i
ans = max(ans, count)

print(N - ans)