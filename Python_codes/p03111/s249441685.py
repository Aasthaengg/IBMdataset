def dfs(i, a, b, c, plus):
    global ans

    if i == n:
        if a and b and c:
            mp = abs(a - A) + abs(b - B) + abs(c - C) + (plus - 3) * 10
            ans = min(ans, mp)

    else:
        dfs(i + 1, a, b, c, plus)
        dfs(i + 1, a + l[i], b, c, plus + 1)
        dfs(i + 1, a, b + l[i], c, plus + 1)
        dfs(i + 1, a, b, c + l[i], plus + 1)


n, A, B, C = map(int, input().split())
l = [int(input()) for i in range(n)]

ans = float("inf")

dfs(0, 0, 0, 0, 0)

print(ans)