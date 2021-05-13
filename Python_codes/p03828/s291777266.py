from collections import defaultdict
n = int(input())

factors = defaultdict(int)
for i in range(2, n + 1):
    for j in range(2, i+1):
        while i % j == 0:
            factors[j] += 1
            i //= j
if n == 1:
    print(1)
else:
    a = '*'.join(str(value+1) for value in factors.values())
    print(eval(a)%(10**9+7))
