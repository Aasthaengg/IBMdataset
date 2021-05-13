from collections import Counter
from itertools import combinations
n, k = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7
inv_num = 0
for left, right in combinations(A, 2):
    if left > right:
        inv_num += 1
#print(inv_num)

acc_num = 0
counter = Counter(A)
rest = n
for key in sorted(counter.keys(), reverse=True):
    rest -= counter[key]
    acc_num += rest * counter[key]

total = (inv_num * k) % mod
total += ((acc_num % mod) * ((k * (k - 1) // 2) % mod)) % mod
total %= mod
print(total)
