import collections
n = int(input())
balls = []
for _ in range(n):
    x, y = map(int, input().split())
    balls.append([x, y])
# print(balls)
delta = []
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dx = balls[j][0] - balls[i][0]
        dy = balls[j][1] - balls[i][1]
        delta.append((dx, dy))

c_delta = collections.Counter(delta)
# print(c_delta)
if len(c_delta):
    print(n-c_delta.most_common()[0][1])
else:
    print(1)