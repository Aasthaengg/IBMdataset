from math import sqrt as r
from math import floor

N = int(input())

ans = 10 ** 20

for i in range(1, floor(r(N)) + 1, 1):
    if N % i == 0:
        a = i - 1
        b = (N // i) - 1
        ans_ = a + b
        ans = min(ans, ans_)

print(ans)
