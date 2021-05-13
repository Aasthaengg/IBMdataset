n, m = map(int, input().split())
xs = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    xs[i] = [a, b]
xs.sort()

cnt = 0
ans = 0
for v in xs:
    if cnt + v[1] < m:
        ans += v[0] * v[1]
        cnt += v[1]
    else:
        print(ans + v[0] * (m - cnt))
        exit()
