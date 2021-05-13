def solve():
    n, k = map(int, input().split())
    a = tuple(map(int, input().split()))

    b = [0] * 50

    for x in a:
        for j in range(50):
            if (x >> j) & 1:
                b[j] += 1

    dp = [-1] * 2
    dp[False] = 0
    # dp[k>=x確定]:=最大値

    for j in reversed(range(50)):
        if (k >> j) & 1:
            # bitを立てられる
            if dp[True] == -1:
                dp[True] = dp[False] + (b[j] << j)
            else:
                dp[True] = max(
                    dp[True] + (max(b[j], n - b[j]) << j),
                    dp[False] + (b[j] << j)
                )
            dp[False] += (n - b[j]) << j
        else:
            # bitを立てられない
            if dp[True] == -1:
                pass
            else:
                dp[True] += max(b[j], n - b[j]) << j
            dp[False] += (b[j] << j)
    return max(dp)


print(solve())
