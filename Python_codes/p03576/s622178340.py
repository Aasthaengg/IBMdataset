n, m = map(int, input().split())
x = [0]*n
y = [0]*n
for i in range(n):
    a, b = map(int, input().split())
    x[i] = a
    y[i] = b

ans = 10**30
for i in range(n):
    for j in range(i):
        for k in range(n):
            for l in range(k):

                left = min(x[i], x[j])
                right = max(x[i], x[j])
                down = min(y[k], y[l])
                up = max(y[k], y[l])

                if left == right or up == down:
                    continue

                cnt = 0
                for r in range(n):
                    if left <= x[r] and x[r] <= right and down <= y[r] and y[r] <= up:
                        cnt += 1
                if cnt >= m:
                    ans = min(ans, (right - left) * (up - down))
print(ans)
