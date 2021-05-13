import sys
input = sys.stdin.readline
mod = 10**9 + 7

n = int(input())
s = input().rstrip()

from collections import Counter

c = Counter(s)

n_ = len(c.keys())

ans = 1

for i in c.keys():
    ans *= (c[i] + 1)
    ans %= mod

ans -= 1

print(ans)