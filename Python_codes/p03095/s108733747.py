import sys
import math
from collections import Counter

N = int(input())
S = input()

MOD = 1000000007

# baba
# a(2), b(2), ab(1), ba(3)

# baab
# a(2), b(2), ab(2), ba(2)

# 1文字の時は分かる、それは単に数えるだけ
# 2文字の時は?
# 'ab' 'a'どれ選ぶ? → その後ろにある'b'は…

# 全部やるなら2^100000、ムリー

# dpいけるか?

# dpを設計しよう
# dp[n] : n文字目まで見た時の答え
# dp[n] = dp[n-1]

# baab
# dp[0] = 1 (b)
# dp[1] = dp[0]((b)のみ選ぶ) + 1(aのみ選ぶ) + dp[0] * 1 (ab)
# それが新しい文字なら?
# dp[n] = dp[n-1](追加で選ばない) + dp[n-1](選ぶ) + 1

# それが見たことある文字なら?
# 1文字単位では増えない
# n文字単位なら、pickする選択肢が増える
# ba (3)
# baa → 3 + 1?
# dp[n] = dp[n] (そのまま) + 最後の文字を使う
# 最後の文字を使うならどうなるか? → それ以外の種類の文字でつくるんだけど大変じゃない????

# baba
# babで5 a, b(2), ab(1) ba(1)
# 最後の文字を使うなら、bをどちらか選ぶ (か、何も選ばない)
# bをpickするか? * どれをpickするか?
# bをpickしない場合(1) + bをpickする場合(どれを選ぶ?)
# (1 + 2)

# abca
# abcで6 a, b, c, ab, ac, bc
# 最後の文字を使うなら、残りのbcの組み合わせ
# bをpickする/しない * cをpickする/しない 4通り?

ans = 1
counter = Counter()
counter[S[0]] += 1

for ch in S[1:]:
    if ch in counter:
        tmp = 1
        for k, cnt in counter.items():
            if k == ch:
                continue

            tmp = (tmp * (1 + cnt)) % MOD

        ans = (ans + tmp) % MOD
        counter[ch] += 1
    else:
        ans = (2 * ans) % MOD
        ans = (ans + 1) % MOD
        counter[ch] += 1

print(ans)

