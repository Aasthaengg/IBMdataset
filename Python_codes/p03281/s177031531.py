import math
import collections
def prime_factor_table(n):
    table = [0] * (n + 1)

    for i in range(2, n + 1):
        if table[i] == 0:
            for j in range(i + i, n + 1, i):
                table[j] = i

    return table

def prime_factor(n, prime_factor_table):
    prime_count = collections.Counter()

    while prime_factor_table[n] != 0:
        prime_count[prime_factor_table[n]] += 1
        n //= prime_factor_table[n]
    prime_count[n] += 1
    keys, values = zip(*prime_count.most_common())

    return values

N = int(input())
table = prime_factor_table(N)
ans = 0
for i in range(1,N+1,2):
    if prime_factor(i,table) == (1,1,1) or prime_factor(i,table) == (3,1) or prime_factor(i,table) == (1,3):
        ans += 1

print(ans)
