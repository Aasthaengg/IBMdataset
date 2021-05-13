def p_k():
    n, k = map(int, input().split())
    *a, = map(int, input().split())

    dp = [False] * (k + 1)
    for i in range(1, k + 1):
        for j in a:
            if i - j >= 0:
                dp[i] |= not dp[i - j]
    print("First" if dp[k] else "Second")


if __name__ == '__main__':
    p_k()
