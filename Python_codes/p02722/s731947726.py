
N = int(input())

def prime_cnt(N):
    # 約数列挙(1,N)も含まれる
    prime, i = set([2]), 1
    while i * i <= N:
        if N % i == 0:
            prime.add(i)
            prime.add(N//i)
        i += 1
    prime.remove(1)
    return prime
import math
ans = 0
ans = prime_cnt(N-1)
p = prime_cnt(N)
for i in p:
    n = N
    while n % i == 0:
        n /= i
    if (n-1) % i == 0:
        ans.add(i)
#print(sorted(list(ans)))
print(len(ans))
