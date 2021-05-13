import fractions
from functools import reduce
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
N = int(input())
A = list(map(int,input().split()))
K = lcm_list(A)
L = K - 1
ans = 0
for i in range(N):
  ans += L % A[i]
print(ans)