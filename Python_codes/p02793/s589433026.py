N = int(input())
A = list(map(int, input().split()))
import math
M = max(A)
MOD = 10 ** 9 + 7

def power_func(a, n, p):
    res = 1 #これは答え
    while n > 0:
        if n & 1:
            res = res * a % p
        a = a * a % p #1が立っているかどうかに関わらず次のaの累乗を用意しておく
        n = n >> 1
    return res

bucket = [0] * (M + 1)
for val in A:
    for i in range(2, math.floor(math.sqrt(val)) + 1):
        #print(val, i)
        temp = 0
        while val % i == 0:
            val //= i
            temp += 1
        bucket[i] = max(bucket[i], temp)
    if val != 1:
        bucket[val] = max(bucket[val], 1)
#print(bucket)

L = 1
for n in range(M + 1):
    L = (L * n ** bucket[n]) % MOD
#print(L)

ans = 0
for val in A:
    ans = (ans + power_func(val, MOD - 2, MOD))
ans = (ans * L) % MOD
print(ans)
