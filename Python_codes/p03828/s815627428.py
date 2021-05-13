# -*- coding: utf-8 -*-
# C - Factors of Factorial
# 標準入力の取得
N = int(input())

# N以下の素数リストを作成
prime_number_list = []
for n in range(2, N+1):
    is_prime_number = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime_number = False
    if is_prime_number:
        prime_number_list.append(n)

# N!の約数の計算
# 各素因数の個数を求め、その個数+1をどんどん掛けていく
result = 1
for pn in prime_number_list:
    n = 1
    count = 0
    while pn**n <= N:
        count += N // (pn**n)
        n += 1
    result *= count + 1

# 結果出力
print(result%(pow(10,9)+7))
