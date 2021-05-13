N, K = map(int, input().split())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())
ans = float('inf')
for x1 in x:
    for x2 in x:
        if x1 > x2:
            continue
        for y1 in y:
            for y2 in y:
                if y1 > y2:
                    continue
                area = (x2 - x1) * (y2 - y1)
                if area >= ans:
                    continue
                cnt = 0
                for i in range(N):
                    if x1 <= x[i] <= x2 and y1 <= y[i] <= y2:
                        cnt += 1
                if cnt >= K:
                    ans = area
print(ans)
