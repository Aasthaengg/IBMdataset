# -*- coding: utf-8 -*-
# 標準入力を取得
N = int(input())


def divisor_count(n: int) -> int:
    ans = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans += 1
            if i != n // i:
                ans += 1
        i += 1
    return ans

# 求解処理
ans = 0
for n in range(1, N + 1, 2):
    if divisor_count(n) == 8:
        ans += 1

# 結果出力
print(ans)