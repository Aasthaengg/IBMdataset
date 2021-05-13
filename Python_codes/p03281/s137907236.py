# -*- coding: utf-8 -*-
# 標準入力を取得
N = int(input())

# 求解処理
ans = 0
for n in range(1, N + 1, 2):
    div_count = 0
    for i in range(1, n + 1):
        div_count += (n % i == 0)

    ans += (div_count == 8)

# 結果出力
print(ans)