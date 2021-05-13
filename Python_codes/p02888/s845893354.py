import itertools
import bisect

N = int(input())
L = list(map(int, input().split(' ')))

L = sorted(L)

count = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        x, y = L[i], L[j]
        limit = x + y
        index = bisect.bisect_left(L, limit)
        count += max(0, index - j - 1)

print(count)