import fractions
from functools import reduce
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_ret_int(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_ret_list(numbers):
    return reduce(lcm_base, numbers, 1)

N = int(input())
*A, = map(int, input().split())
lcm_n = lcm_ret_int(*A) - 1
ans = 0
for i in range(N):
    ans += lcm_n % A[i]
print(ans)