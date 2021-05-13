from collections import defaultdict as dd
from sys import exit
import math
n, m = map(int, input().split())
dic = dd(int)

#M=1
if m == 1:
    print(1)
    exit()

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i in range(2, math.ceil(m**0.5) + 3):
    while m % i == 0:
        m //= i
        dic[i] += 1
if m != 1:
    dic[m] = 1
#print(dic)

ans = 1
mod = 10**9 + 7
for count in dic.values():
    ans *= combinations_count(count + n - 1, n-1) % mod

print(ans % mod)