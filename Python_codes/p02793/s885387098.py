import math
import sys
input = sys.stdin.readline

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

N = int(input())
A = list(map(int, input().split()))

mod = 10**9 + 7
# A全体の最小公倍数
a_lcm = 1
for a in A:
    a_lcm = lcm(a_lcm, a)

# Bの総和
b_sum = 0
for i in range(N):
    b_sum += a_lcm // A[i]

print(b_sum % mod)
