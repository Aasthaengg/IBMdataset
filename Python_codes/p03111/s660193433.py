n, a, b, c = map(int,input().split())
l = [int(input()) for i in range(n)]
INF = 10 ** 9

def dfs(i, x, y, z):
    if i == n:
        cand = abs(a - x) + abs(b - y) + abs(c - z) - 30 if min(x, y, z) > 0 else INF
        return cand

    temp0 = dfs(i + 1, x + l[i], y, z) + 10
    temp1 = dfs(i + 1, x, y + l[i], z) + 10
    temp2 = dfs(i + 1, x, y, z + l[i]) + 10
    temp3 = dfs(i + 1, x, y, z)
    return min(temp0, temp1, temp2, temp3)

ans = dfs(0,0,0,0)
print(ans)