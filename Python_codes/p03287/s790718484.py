import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

from itertools import accumulate
cumsum_a = [0] + list(accumulate(a))
for i in range(len(cumsum_a)):
    cumsum_a[i] %= m

from collections import Counter

c = Counter(cumsum_a)

ans = 0

for i in c.keys():
    ans += c[i] * (c[i] - 1) // 2

print(ans)