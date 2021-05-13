# A - Colorful Subsequence AC (hint)
import collections
N = int(input())
S = input()
MOD = 10**9+7

cnt = collections.Counter(S)

# 文字の選び方
# 1 個選ぶ or 2 選ぶ or 3 個選ぶ or ... cnt 個選ぶ or 選ばない
# (cnt + 1) 通り
ans = 1
for value in cnt.values():
    ans = (ans*(value+1))%MOD
print(ans - 1)