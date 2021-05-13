# 解説版

from collections import defaultdict
N, K = map(int, input().split())
balls = defaultdict(int)
for b in input().split():
    balls[b] += 1
balls = sorted(balls.values())
print(N - sum(balls[-K:]))
