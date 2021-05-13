# https://atcoder.jp/contests/agc031/tasks/agc031_a

from collections import Counter
n = int(input())
s = input()
mod = 10 ** 9 + 7

ans = 1
c = Counter(s)
for v in c.values():
    ans = ans * (v + 1) % mod

print(ans - 1)