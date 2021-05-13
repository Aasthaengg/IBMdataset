N = int(input())

def sieve(N):
    p = 0
    prime = []
    is_prime = [1 for _ in range(N + 1)]
    is_prime[0], is_prime[1] = 0, 0
    for i in range(2, N + 1):
        if is_prime[i]:
            p += 1
            temp = i
            prime.append(i)
            while(temp <= N):
                is_prime[temp] = 0
                temp += i
            is_prime[i] = 1
    return p, prime

def fact_prime(n, p):
    ret = 0
    temp = p
    while(n >= p):
        ret += n // p
        p *= temp
    return ret

_, prime_list = sieve(N)
ans = 0

for a in prime_list:
    for b in prime_list:
        for c in prime_list:
            if a != b and b < c and a != c:
                if fact_prime(N, a) >= 2 and fact_prime(N, b) >= 4 and fact_prime(N, c) >= 4:
                    ans += 1
                    
for a in prime_list:
    for b in prime_list:
        if b != a:
            if fact_prime(N, a) >= 24 and fact_prime(N, b) >= 2:
                ans += 1
            if fact_prime(N, a) >= 4 and fact_prime(N, b) >= 14:
                ans += 1
                
for a in prime_list:
    if fact_prime(N, a) >= 74:
        ans += 1    

print(ans)