#!/usr/bin/env python3
import sys

sys.setrecursionlimit(1000000)


memo = [0]*(10**5+1)
def count(n):
    if n < 2:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = count(n-1) + count(n-2)
    return memo[n]


n, m, *a = map(int, open(0).read().split())
if sum(a[i + 1] == a[i] + 1 for i in range(m - 1)) > 0:
    print(0)
    exit()

a.append(n + 1)
c = -1
ans = 1
for i in a:
    ans = ans * count(i - c - 2) % (10**9 + 7)
    c = i
print(ans)
