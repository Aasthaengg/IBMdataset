# D - 756
from collections import defaultdict

N = int(input())

def prime_factorization(n):
    prime_factors = []
    if n < 2:
        return 0
    for i in range(2, int(pow(n, 0.5)+1)):
        if n%i==0:
            ex = 0
            while n%i==0:
                ex += 1
                n //= i
            prime_factors.append((i, ex))
    # 割り切れなかった残りのnが1でない(素数)場合、リストに加える
    if n!=1:
        prime_factors.append((n,1))
    return prime_factors

primes = defaultdict(int)
for i in range(2, N+1):
    p = prime_factorization(i)
    for (j, k) in p:
        primes[j] += k

primes = list(primes.values())
l = len(primes)

ans = 0
arr = []
def dfs(n, x, s):
    global ans
    if x == l:
        if s == 75:
            ans += 1
        return
    for i in range(min(primes[x]+1, 75//s)):
        if i in (0, 2, 4, 14, 24, 74):
            n.append(i)
            dfs(n, x+1, s*(i+1))
            n.pop()
    return

dfs(arr, 0, 1)
print(ans)