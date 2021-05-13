from functools import reduce

n = int(input())
mod = 10**9 +7
ans = reduce(lambda total, x: total * x % mod, range(1, n+1))

print(ans)