# coding: utf-8
# Your code here!

from collections import Counter

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
  
n = int(input())
x = Counter(prime_factorize(n))
x_keys = list(x.keys())
x_values = list(x.values())
ans = 0
for i in range(len(x_keys)):
    z = x_values[i]
    mai = 1
    while z - mai >= 0:
        z -= mai
        mai += 1
        ans += 1
print(ans)        
