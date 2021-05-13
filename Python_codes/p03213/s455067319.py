from collections import defaultdict


def factorize(N):  # 素因数分解
    p = 2 
    while p * p <= N:
        while N % p == 0:
            N //= p
            fact[p] += 1
        p += 1
    if N > 1:
        fact[N] += 1

n = int(input())
fact = defaultdict(int)
for i in range(n):
    factorize(i + 1)

cnt4 = sum(cnt >= 4 for cnt in fact.values())
cnt2 = sum(cnt >= 2 for cnt in fact.values())
cnt24 = sum(cnt >= 24 for cnt in fact.values())
cnt14 = sum(cnt >= 14 for cnt in fact.values())
cnt74 = sum(cnt >= 74 for cnt in fact.values())

ans = cnt4 * (cnt4 - 1) * (cnt2 - 2) // 2
ans += cnt24 * (cnt2 - 1) + (cnt4 - 1) * cnt14 + cnt74
print(ans)
