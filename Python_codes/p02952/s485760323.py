# 問題：https://atcoder.jp/contests/abc136/tasks/abc136_b

n = int(input())
ln_n = len(str(n))
if ln_n % 2 == 0:
    n = 10 ** (ln_n - 1) - 1

res = 0
for i in range(1, ln_n):
    if i % 2 == 1:
        res += 10 ** i - 10 ** (i - 1)
res += n + 1 - 10 ** (ln_n - 1)

print(res)
