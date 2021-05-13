from bisect import bisect_left, bisect_right
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(3,n + 1) if is_prime[i]]

prime = primes(10**5)
p_set = set(prime)
like = [3]
for i in prime:
    if (i+1)//2 in p_set:
        like.append(i)

Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    print(bisect_right(like, r) - bisect_left(like, l))