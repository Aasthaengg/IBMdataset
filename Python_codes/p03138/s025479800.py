def solve():
    n, k = map(int, input().split())
    a = tuple(map(int, input().split()))

    x = [[0] * 2 for _ in range(50)]
    # x[j][0]:=bit_jをxで立てない
    # x[j][1]:=bit_jをxで立てる

    for j in range(50):
        b = sum(1 for x in a if (x >> j) & 1)
        x[j][0] = b << j
        x[j][1] = (n - b) << j

    dp = [-1] * 2
    dp[False] = 0
    # dp[k>=x確定]:=最大値

    for j in reversed(range(50)):
        if (k >> j) & 1:
            # bitを立てられる
            if dp[True] == -1:
                dp[True] = dp[False] + x[j][0]
            else:
                dp[True] = max(dp[True] + max(x[j]), dp[False] + x[j][0])
            dp[False] += x[j][1]
        else:
            # bitを立てられない
            if dp[True] == -1:
                pass
            else:
                dp[True] += max(x[j])
            dp[False] += x[j][0]
    return max(dp)


print(solve())
