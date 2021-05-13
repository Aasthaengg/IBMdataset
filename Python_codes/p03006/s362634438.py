n = int(input())
ball = []
for i in range(n):
    ball.append(list(map(int, input().split())))

ans = 1000
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        temp = 0
        x0, y0 = ball[i]
        x1, y1 = ball[j]
        p, q = x1-x0, y1-y0
        used = [False]*(n)
        for k in range(n):
            if not used[k]:
                temp += 1
                x0, y0 = ball[k]
                used[k] = True

                x, y = x0, y0
                while True:
                    f = 0
                    for l in range(n):
                        if used[l]:
                            continue
                        if x + p == ball[l][0] and y + q == ball[l][1]:
                            used[l] = True
                            x += p
                            y += q
                            f = 1
                    if f == 0:
                        break

                x, y = x0, y0
                while True:
                    f = 0
                    for l in range(n):
                        if used[l]:
                            continue
                        if x - p == ball[l][0] and y - q == ball[l][1]:
                            used[l] = True
                            x -= p
                            y -= q
                            f = 1
                    if f == 0:
                        break

        ans = min(ans, temp)

if n == 1:
    print(1)
else:
    print(ans)
