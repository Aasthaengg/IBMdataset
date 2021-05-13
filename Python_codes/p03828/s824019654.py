import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
MOD = 10 ** 9 + 7
prime_factors = dict()

for i in range(1, n+1):
    j = 2
    while j ** 2 <= i:
        ext = 0
        while i % j == 0:
            ext += 1
            i //= j
        if j in prime_factors:
            prime_factors[j] += ext
        else:
            prime_factors[j] = ext
        j += 1
    if i != 1:
        if i in prime_factors:
            prime_factors[i] += 1
        else:
            prime_factors[i] = 1

ans = 1
for pf in prime_factors:
    ans = (ans * (prime_factors[pf] + 1)) % MOD
print(ans)
