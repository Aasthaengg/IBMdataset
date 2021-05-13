import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
MOD = 10 ** 9 + 7

prime_factories = [0] * (n+1)
for i in range(2, n+1):
    j = 2
    while j ** 2 <= i:
        ext = 0
        while i % j == 0:
            ext += 1
            i //= j
        if ext:
            prime_factories[j] += ext
        j += 1
    if i != 1:
        prime_factories[i] += 1
ans = 1
# 合成数のnumは0、num+1=1の乗算は計算結果に影響しない
for num in prime_factories:
    ans = (ans * (num + 1)) % MOD
print(ans)
