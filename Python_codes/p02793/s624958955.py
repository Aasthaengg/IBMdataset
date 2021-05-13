from fractions import gcd

from functools import reduce


n = int(input())
a_list = [int(x) for x in input().split()]

temp = 1
for a in a_list:
    temp *= a // gcd(a, temp)

ans = 0
for a in a_list:
    ans += temp // a
mod = 10 ** 9 + 7
ans %= mod

print(ans)