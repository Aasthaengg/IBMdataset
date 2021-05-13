from collections import defaultdict

res = defaultdict(lambda: 0)
#素因数分解O(√n)
def primeFactor(n):
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            res[i] += 1
            n = n // i
    if n != 1:
        res[n] += 1

N = int(input())

for i in range(1, N+1):
    primeFactor(i)

ans = 1
for v in res.values():
    ans *= (v+1)
    ans %= 10**9+7

print(ans)


