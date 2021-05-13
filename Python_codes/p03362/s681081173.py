def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    p = 0
    for i in range(2,n+1):
        if is_prime[i]:
            p = i
            for j in range(p+p, n+1, p):
                is_prime[j] = False
        
        if p * p > n:
            break
    
    primes = []
    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)

    return primes

def solve():
    N = int(input())
    primes = sieve(55555)
    ans = []
    for prime in primes:
        if prime % 5 == 1:
            ans.append(str(prime))

        if len(ans) == N:
            break
    
    print(" ".join(ans))

if __name__ == '__main__':
    solve()