n = int(input())
primes = []
def is_prime(k):
    if k < 2:
        return False
    if k == 2:
        return True
    for p in primes:
        if k % p == 0:
            return False
        if k <= p*p:
            break
    return True


for i in range(1000000 + 100):
    if is_prime(i):
        primes.append(i)
        if i >= n:
            print(i)
            break
