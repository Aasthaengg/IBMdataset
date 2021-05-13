import collections
N, M = map(int, input().split())
mod = pow(10, 9) + 7

def prime_factorize(K):
    ans = []
    i = 2
    while i ** 2 <= K:
        if K % i == 0:
            K //= i
            ans.append(i)
        else:
            i += 1
    if K != 1:
        ans.append(K)
    
    return ans

def combination(N, r):
    ans = N
    for i in range(1, r):
        ans *= ((N - i) % mod) * pow(i + 1, mod - 2, mod)
        ans %= mod
    
    return ans

prime_nums = dict(collections.Counter(prime_factorize(M)))

ans = 1
for num in prime_nums.values():
    ans *= combination(N - 1 + num, num)
    ans %= mod

print(ans)