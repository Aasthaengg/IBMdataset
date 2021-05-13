# https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_b

n = int(input())
ball = []
s = set()
for _ in range(n):
    x, y = map(int, input().split())
    ball.append((x, y))
    s.add((x, y))

ans = n
for i in range(n):
    x, y = ball[i]
    for j in range(n):
        dx, dy = x - ball[j][0], y - ball[j][1]
        if dx == 0 and dy == 0:
            continue
        point = 0
        for k in range(n):
            a, b = ball[k][0] - dx, ball[k][1] - dy
            if (a, b) in s:
                point += 1
        ans = min(ans, n - point)
print(ans)