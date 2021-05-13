#089_D
h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
idx = {}
for x in range(0, h):
    for y in range(0, w):
        idx[a[x][y]] = (x, y)
        
dp = [0 for _ in range(h*w+1)]
for i in range(0, h*w+1):
    if i <= d:
        continue
    x, y = idx[i]
    x_, y_ = idx[i-d]
    dp[i] = dp[i-d] + abs(x-x_) + abs(y-y_)
        
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(dp[r] - dp[l])