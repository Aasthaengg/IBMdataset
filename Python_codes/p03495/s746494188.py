from collections import defaultdict
N, K = map(int, input().split())
balls = defaultdict(int)
for b in input().split():
    balls[b] += 1
types = len(balls.keys())
balls = sorted(balls.values(), reverse=True)
ans = 0
while types > K:
    ans += balls.pop()
    types -= 1
print(ans)
