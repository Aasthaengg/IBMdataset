# -*- coding: utf-8 -*-
# 標準入力を取得
n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

# メイン処理
ans_list = ["no" for i in range(q)]
for bit in range(1 << n):
    s = 0
    for i in range(n):
        if bit & (1 << i):
            s += A[i]
    L = [i for i, x in enumerate(m) if x == s]
    for l in L:
        ans_list[l] = "yes"

# 結果出力
for ans in ans_list:
    print(ans)
