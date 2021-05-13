# 組み合わせ計算
# 約分してから計算するアルゴリズム
# 10^9 + 7 で割ったあまりを返すバージョン
MOD = 1000000007

def combination(n, r):
    # n >= 0, r >= 0, r <= n を仮定
    if n < 0 or r < 0 or n < r:
        return -1

    # r <= n - r を仮定
    if n - r < r:
        r = n - r

    # r < 2 の場合
    if r == 0:
        return 1
    if r == 1:
        return n

    # nCr の分子
    # [n - r + 1, n - r + 2, ... , n - 1, n]
    numerator = [n - r + 1 + i for i in range(r)]


    # nCr の分母
    # [1, 2, ... , r - 1, r]
    denominator = [i + 1 for i in range(r)]

    # nCr を約分する
    for i in range(r):
        # i番目の分母で約分する
        # 0番目は1なので省略

        # 元の（今までの約分を行う前の）i番目の分母の値
        original_denominator = i + 1

        # 今までの約分を行った後の、i番目の分母の値
        # 今回の約分で割る数
        divisor = denominator[i]

        # divisorが1（全て約分済み）の場合は無視する
        if divisor == 1:
            continue

        # 約分する相手の分子を決める
        # 0～i番目の分子（約分前）の中で、
        # original_denominatorで割り切れる数
        # （一つしかない）を選ぶ
        # remainder = i番目の分子 % original_denominator
        # とするとき、
        # (i - remainder)番目の分子 = i番目の分子 - remainder
        # (i - remainder)番目の分子 % original_denominator
        #  = (i番目の分子 - remainder) % original_denominator
        #  = 0
        # なので、(i - remainder)番目の分子を選べばよい。

        # remainder = i番目の分子 % original_denominator
        #           = (n - r + i + 1) % (i + 1)
        #           = (n - r) % (i + 1)
        remainder = (n - r) % original_denominator

        # divisor で約分できるペアをすべて約分する
        for j in range(i, r, original_denominator):
            numerator[j - remainder] = numerator[j - remainder] // divisor
            denominator[j] = denominator[j] // divisor

    ans = 1
    for i in numerator:
        ans = (ans * i) % MOD
    return ans


N, K = map(int, input().split())
for i in range(1, K + 1):
    if N - K + 1 >= i:
        print(combination(N - K + 1, i) * combination(K - 1, i - 1) % MOD)
    else:
        print(0)