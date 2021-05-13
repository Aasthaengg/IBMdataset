from collections import defaultdict

N, M = map(int, input().split())

memo = [0]*N

for _ in range(M):
    a, b = map(int, input().split())
    memo[a-1] += 1
    memo[b-1] += 1

print(*memo, sep="\n")