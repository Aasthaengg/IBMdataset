from collections import Counter
import math
def nCr(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, a, b = map(int, input().split())

values = [int(i) for i in input().split()]
values.sort(reverse=True)

MAX = sum(values[:a]) / a
print(MAX)
e = a + 1
use_nums = []
for i in range(a, b + 1):
    v = sum(values[:i]) / i
    if v == MAX:
        use_nums.append(Counter(values[:i]))

cd = Counter(values)
ans = 0
for nums in use_nums:
    t = 1
    for k, v in nums.items():
        m = cd.get(k)
        t = t * nCr(m, v)
    ans += t
print(ans)