a, b, c, d, e, f = map(int, input().split())

ans = (0, 100*a)
def dfs(c_s,c_w, idx):
    global ans
    if idx == 4:
        if c_w + c_s > f:
            return
        if e*(c_w // 100) < c_s:
            return
        if c_w+c_s == 0:
            return
        if c_s / (c_w+c_s) > ans[0] / (ans[0]+ans[1]):
            ans = (c_s, c_w)
    else:
        t = [a, b, c, d][idx]
        for i in range(((f-(c_s+c_w)) // t)+1):
            if idx <= 1:
                dfs(c_s, c_w + 100 * t * i, idx + 1)
            else:
                dfs(c_s + t*i, c_w, idx + 1)
dfs(0, 0, 0)
print(*[ans[0]+ans[1], ans[0]])