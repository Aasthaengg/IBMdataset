# dfs版
def dfs(d, A, B, C, f):
    global ans
    if d == n:
        if not 0 in [A, B, C]:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) + f - 30)
        return
    dfs(d + 1, A, B, C, f)
    dfs(d + 1, A + l[d], B, C, f + 10)
    dfs(d + 1, A, B + l[d], C, f + 10)
    dfs(d + 1, A, B, C + l[d], f + 10)


n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = 10 ** 10
dfs(0, 0, 0, 0, 0)
print(ans)
