s = input()
x, y = map(int, input().split())

mv = [len(e) for e in s.split("T")]
mv_x = mv[2::2]
mv_y = mv[1::2]


def solve_dp(li, start, end):
    l = len(li)
    mx = sum(li)

    if l == 0:
        return start == end

    left = start - mx
    right = start + mx

    if end > right or end < left:
        return 0

    dp = [[0] * (2 * mx + 1) for _ in range(l + 1)]
    dp[0][start] = 1
    for i, e in enumerate(li, 1):
        for j in range(left, right + 1):
            if left <= j - e <= right:
                dp[i][j] |= dp[i-1][j-e]
            if left <= j + e <= right:
                dp[i][j] |= dp[i-1][j+e]

    return dp[l][end]


bl_x = solve_dp(mv_x, mv[0], x)
bl_y = solve_dp(mv_y, 0, y)

if bl_x and bl_y:
    ans = "Yes"
else:
    ans = "No"

print(ans)
