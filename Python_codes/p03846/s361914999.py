# -*- coding: utf-8 -*-
# C - Lining Up
# 標準入力の取得
N = int(input())
A_list = list(map(int, input().split()))
sorted_A_list = sorted(A_list)

# 期待されるA_listの算出
EXPECTED_LIST = []
is_N_even = (N % 2 == 0)
for n in range(N):
    is_n_even = (n % 2 == 0)
    if is_N_even:
        # Nが偶数の場合、[1, 1, 3, 3, ・・・, N-1, N-1]となる
        if is_n_even:
            EXPECTED_LIST.append(n+1)
        else:
            EXPECTED_LIST.append(n)
    else:
        # Nが奇数の場合、[0, 2, 2, 4, 4, ・・・, N-1, N-1]となる
        if is_n_even:
            EXPECTED_LIST.append(n)
        else:
            EXPECTED_LIST.append(n+1)

# 判定処理
if sorted_A_list == EXPECTED_LIST:
    # 報告が正しかった場合、並び方の総数を10^9+7で割った余りを出力
    print(2**(N//2) % (pow(10, 9)+7))
else:
    # 報告が誤りであった場合、0を出力して、処理を終了する
    print(0)