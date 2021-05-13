N = int(input())
S = list(input())

MOD = 10 ** 9 + 7

from collections import Counter

Scnt = Counter(S)

# 任意の文字列について、
# どれかを取り出す or どれも取り出さない

ans = 1
for cnt in Scnt.values():
    ans = (ans * (cnt + 1)) % MOD

ans -= 1

print(ans)