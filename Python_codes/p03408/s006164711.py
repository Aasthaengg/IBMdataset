# -*- coding: utf-8 -*-

# input
N = int(input())
s = []

for i in range(N):
    s.append(str(input()))

M = int(input())
t = []

for j in range(M):
    t.append(str(input()))

set_s = set(s)
set_t = set(t)
ans = 0
tmp_ans = 0

for tmp_s in set_s:
    # 演算
    tmp_ans = s.count(tmp_s) - t.count(tmp_s)
    # 最大値判定
    ans = max(ans, tmp_ans)

print(ans)