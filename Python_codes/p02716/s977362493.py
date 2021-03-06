from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

dp = defaultdict(lambda: -float('inf'))
dp[(0, 0, 0)] = 0

for i, a in enumerate(A, start=1):
    j = i // 2
    for x in range(j - 1, j + 2):
        dp[(i, x, 0)] = max(dp[(i - 1, x, 0)], dp[(i - 1, x, 1)])
        dp[(i, x, 1)] = dp[(i - 1, x - 1, 0)] + a

print(max(dp[(N, N // 2, 0)], dp[(N, N // 2, 1)]))