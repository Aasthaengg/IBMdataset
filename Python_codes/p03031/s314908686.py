# -*- coding: utf-8 -*-
# 標準入力を取得
N, M = list(map(int, input().split()))
k, s = [], []
for m in range(M):
    l = list(map(int, input().split()))
    k.append(l[0])
    s.append(l[1:])
p = list(map(int, input().split()))

# 求解処理
ans = 0
for bit in range(1 << N):
    is_light_on = True
    for m in range(M):
        on_count = 0
        for s_i in s[m]:
            if ((bit >> (s_i - 1)) & 1):
                on_count += 1
        if on_count % 2 != p[m]:
            is_light_on = False
            break
    if is_light_on:
        ans += 1

# 結果出力
print(ans)
