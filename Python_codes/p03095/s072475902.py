from collections import Counter
N = int(input())
C = Counter(input())

mod = 10 ** 9 + 7
ans = 1
for v in C.values():
    ans *= (v + 1)  # 使う:v通り、使わない1通り
    ans %= mod

ans -= 1
print(ans % mod)