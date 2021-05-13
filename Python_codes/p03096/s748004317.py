import sys

input = sys.stdin.readline

n = int(input())
mod = 10 ** 9 + 7

c = []

for i in range(n):
    c.append(int(input()))

d = {}
dp = [[1,0]]

p = -1
for ci in c:
    if p != ci:
        cnt = 0
        if ci in d:
            cnt = sum(dp[d[ci]]) % mod
        dp.append([sum(dp[-1]) % mod, cnt])
        d[ci] = len(dp) - 1
    p = ci

print(sum(dp[-1]) % mod)
