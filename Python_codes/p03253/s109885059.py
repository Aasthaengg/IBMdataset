from scipy.misc import comb
# from scipy.special import comb


N, M = map(int, input().split())
MOD = 10**9+7
# M を素因数分解
rest = M
ans = 1
for i in range(2, int(M ** 0.5) + 1):
    cnt = 0
    while rest % i == 0:
        cnt += 1
        rest //= i
    # cnt が 2^X 1とか 3^X の X の部分
    ans *= comb(N+cnt-1, N-1, exact=True)
    ans %= MOD
if rest != 1:
    cnt = 1
    ans *= comb(N+cnt-1, N-1, exact=True)
    ans %= MOD

print(ans)
