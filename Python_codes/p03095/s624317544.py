from collections import Counter

N = int(input())
S = str(input())
MOD = 10 ** 9 + 7
ans = 1

for v in Counter(S).values():
    ans *= v + 1
    ans %= MOD

print(ans - 1) # 文字列の長さが 0 の場合を引く 