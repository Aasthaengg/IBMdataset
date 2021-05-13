
L = input()
MOD = 10 ** 9 + 7

num = 0
res = 0
n = len(L)
for i in range(n):
    length = n - i - 1
    if L[i] == "1":
        res = (res + pow(2, num, MOD) * pow(3, length, MOD))
        num += 1

res = (res + pow(2, num, MOD)) % MOD
print(res)
