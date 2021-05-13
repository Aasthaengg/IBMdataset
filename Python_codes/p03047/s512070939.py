'''
A - Consecutive Integers
'''

import itertools

n, k = map(int, input().split())

ans = 0
for i in range(1, n+1):
    if i + k - 1 <= n:
        ans += 1

print(ans)
