from math import sqrt, factorial

n = int(input())

MAX_VAL = n
prime = [1] * (MAX_VAL+1)
prime[0] = prime[1] = 0
for i in range(2, int(sqrt(MAX_VAL))+1):
    if prime[i]:
        for k in range(2*i, MAX_VAL+1, i):
            prime[k] = 0

res = 1
for i, p in enumerate(prime):
    m = factorial(n)
    if p:
        cnt = 0
        while m % i == 0:
            cnt += 1
            m //= i
        res *= cnt + 1
        res %= 10**9+7

print(res)
