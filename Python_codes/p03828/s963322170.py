def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n%i == 0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass


n = int(input())

prime = []
for i in range(2, n+1):
    prime = prime + prime_factor(i)

from collections import Counter

primec = Counter(prime)

ans = 1

primec_list = primec.most_common()

mod = 10**9+7

for p in primec_list:
    ans = ans * (p[1]+1) % mod

print(ans)