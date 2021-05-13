import itertools
import math
import functools

K = int(input())

ans = 0

for i in itertools.product(range(1,K+1),repeat=3):
    ans += functools.reduce(math.gcd,i)
print(ans)
