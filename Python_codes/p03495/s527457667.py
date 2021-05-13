n, k = map(int, input().split())
a = list(map(int, input().split()))
ball = {}

for i in a:
    if i in ball:
        ball[i] += 1
    else:
        ball[i] = 1

ball = sorted(ball.items(), key=lambda x: -x[1])

ans = 0
if len(ball) > k:
    for i in range(k):
        ans += ball[i][1]
    ans = n - ans
print(ans)
