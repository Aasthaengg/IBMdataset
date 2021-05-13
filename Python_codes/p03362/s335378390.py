n = int(input())

#n以下の素数列挙(O(n log(n))
def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i] and i % 5 == 1:
            ass.append(i)
    return ass

prime_list = primes(55555)
#print(prime_list)
#print(len(prime_list))
ans = []
for i in range(n):
    ans.append(prime_list[i])
print(*ans)