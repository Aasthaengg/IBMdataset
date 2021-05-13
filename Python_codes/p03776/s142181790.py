from collections import Counter
import math
n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
MAX = sum(v[:a]) / a
print(MAX)

c = Counter(v)
average_nums = []
for i in range(a, b + 1):
    t = sum(v[:i]) / i
    if t >= MAX:
        average_nums.append(Counter(v[:i]))

def nCr(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = 0
for num in average_nums:
    multi = 1
    for k, v in num.items():
        multi = multi * nCr(c[k], v)
    ans += multi
print(ans)