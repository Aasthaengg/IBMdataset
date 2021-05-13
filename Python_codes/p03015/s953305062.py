import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

L = list(sr())
MOD = 10 ** 9 + 7
bit_len = len(L)

dp_any = 1 # 1桁目が(0, 0)の組み合わせ, dp_any はi+1桁目がどんな数字でも条件を満たす
dp_spe = 2
for i in range(1, bit_len):
    x, y = dp_any, dp_spe
    if L[i] == '1':
        dp_any = x * 3 + y
        dp_spe = y * 2
    else:
        dp_any = x * 3
        dp_spe = y
    dp_any %= MOD
    dp_spe %= MOD

answer = (dp_any + dp_spe) % MOD
print(answer)
