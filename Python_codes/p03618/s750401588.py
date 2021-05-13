import collections

A = list(input())
N, ans = len(A), 0

c = collections.Counter(A)
for x in list(c.keys()):
    ans += c[x] * (c[x] - 1) // 2

print(N*(N-1)//2 + 1 - ans)