import sys

def I(): return int(sys.stdin.readline().rstrip())

N = I()
mod = 10**9+7

import math

def sieve_of_eratosthenes(n):
    prime_list = []  # n以下の素数のリスト
    A = [1]*(n+1)    # A[i] = iが素数なら1,その他は0
    A[0] = A[1] = 0
    for i in range(2,math.floor(math.sqrt(n))+1):
        if A[i]:
            prime_list.append(i)
            for j in range(i**2,n+1,i):
                A[j] = 0
    for i in range(math.floor(math.sqrt(n))+1,n+1):
        if A[i] == 1:
            prime_list.append(i)
    return prime_list

prime_list = sieve_of_eratosthenes(N)

ans = 1
for p in prime_list:
    a = 0
    r = N
    while r >= p:
        a += r//p
        r //= p
    ans *= a+1
    ans %= mod

print(ans)