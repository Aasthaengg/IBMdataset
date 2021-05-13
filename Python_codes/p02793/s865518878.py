import sys
from collections import Counter

def prime_factorize(n):
    ans = []
    while not n%2:
        ans.append(2)
        n //= 2
    mod = 3
    while mod**2 <= n:
        if n%mod == 0:
            ans.append(mod)
            n //= mod
        else:
            mod += 2
    if n != 1:
        ans.append(n)
    counter = Counter(ans)
    return counter

def main():
    input = sys.stdin.readline
    mod = pow(10,9)+7
    n = int(input())
    a = [int(x) for x in input().split()]
    
    prime_list = dict()
    for i in range(n):
        primes = prime_factorize(a[i])
        for key, value in primes.items():
            if key in prime_list:
                if prime_list[key] < value:
                    prime_list[key] = value
            else:
                prime_list[key] = value
    
    L = 1
    for key, value in prime_list.items():
        L *= pow(key, value, mod)
        L %= mod
        
    ans = 0
    for i in range(n):
        ans += (L*pow(a[i], mod-2, mod))%mod
        ans %= mod
    
    print(ans)

if __name__ == "__main__":
    main()