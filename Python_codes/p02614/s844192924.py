import itertools

# -*- coding: utf-8 -*-
# 整数の入力
H, W, K = map(int, input().split())
# 文字列の入力
masu_list = []
for i in range(H):
    str = input()
    masu_list.append(list(str))
ans = 0

for H_bit in range(1 << H):
    for W_bit in range(1 << W):
        break_i = 0
        cnt = 0
        for i in range(H):
            if break_i == 1:
                break
            for j in range(W):
                if (H_bit >> i) & 1 and (W_bit >> j) & 1:
                    if masu_list[i][j] == "#":
                        cnt += 1
                        if cnt > K:
                            break_i = 1
                            break
        if cnt == K:
            ans += 1
print(ans)
