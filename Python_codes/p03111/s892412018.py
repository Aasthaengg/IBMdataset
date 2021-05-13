n, a, b, c = map(int, input().split())
ll = [int(input()) for _ in range(n)]

def dfs(cnt, x, y, z):
    if cnt == n:
        if x == 0 or y == 0 or z == 0:
            return float('INF')
        return abs(a - x) + abs(b - y) + abs(c - z) - 30
    r0 = dfs(cnt + 1, x, y, z)
    r1 = dfs(cnt + 1, x + ll[cnt], y, z) + 10
    r2 = dfs(cnt + 1, x, y + ll[cnt], z) + 10
    r3 = dfs(cnt + 1, x, y, z + ll[cnt]) + 10
    return min(r0, r1, r2, r3)

print(dfs(0, 0, 0, 0))