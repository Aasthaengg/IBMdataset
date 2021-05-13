import math
from itertools import combinations_with_replacement

n, p = map(int, input().split())
A = list(map(int, input().split()))
odd = []
even = []


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)
even_count = []
for i in range(len(even)+1):
    even_count.append(combinations_count(len(even), i))
odd_odd_count = []
odd_even_count = []
for i in range(len(odd)+1):
    cnt = combinations_count(len(odd), i)
    if i % 2 == 1:
        odd_odd_count.append(cnt)
    else:
        odd_even_count.append(cnt)
ans = 0
if p == 0:
    for i in even_count:
        for j in odd_even_count:
            ans += i*j
else:
    for i in even_count:
        for j in odd_odd_count:
            ans += i*j

print(ans)
