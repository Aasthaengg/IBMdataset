N = int(input())
S = input()
from collections import Counter
c = Counter(S)
p = 10**9 + 7
result = 1
for v in c.values():
    result *= (v+1)
    result %= p
print((result - 1) % p)