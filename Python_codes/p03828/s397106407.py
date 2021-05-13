N = int(input())

import math

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

num = prime_factorize(math.factorial(N))
ans = 1
num_list = set(num)

mod = 10**9+7

for x in num_list:
    ans = ans*(num.count(x)+1)%mod
    
print(ans)