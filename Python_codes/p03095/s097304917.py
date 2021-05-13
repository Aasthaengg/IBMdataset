from collections import Counter
import itertools as it
MOD = 10 ** 9 + 7
n = int(input())
s = input()

b = Counter(s)
c = list(b)

ans = 1
for i in b:
    ans = ans * (b[i]+1) % MOD
    
print((ans + MOD - 1) % MOD)