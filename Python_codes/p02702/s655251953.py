import sys
input = sys.stdin.readline
mod = 2019

s = input().strip()[::-1]
l = [0] * mod

n10 = [1]
for _ in range(len(s)):
    n10.append(n10[-1] * 10 % mod)

n = 0
for i, c in enumerate(s):
    n += n10[i] * int(c)
    n %= mod
    l[n] += 1

ans = 0
for i, v in enumerate(l):
    if v > 1:
        ans += v * (v - 1) // 2
    if i == 0:
        ans += v
print(ans)
