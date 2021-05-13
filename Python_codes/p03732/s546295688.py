import sys
def input(): return sys.stdin.readline().strip()
offset = 10**10

def main():
    N, W = map(int, input().split())
    w0, v0 = map(int, input().split())
    item = [0, w0 * offset + v0]
    weight_sum, value_sum = w0, v0
    for _ in range(1, N):
        w, v = map(int, input().split())
        item.append(w * offset + v)
        weight_sum += w
        value_sum += v

    if W < w0:
        print(0)
        return
    if weight_sum <= W:
        print(value_sum)
        return

    if w0 <= 3 * (N - 1):
        # dp[i][j] = (1~i番目の荷物を重さj以下で詰めたときの最大価値)
        dp = [[0] * (W + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            w, v = item[i] // offset, item[i] % offset
            for j in range(w): dp[i][j] = dp[i - 1][j]
            for j in range(w, W + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        print(dp[N][W])
        return

    # dp[i][j][k] = (1~i番目までのものを見たとき、重さが(j * w0 + k)以下で最大価値がいくらか)
    dp = [[[0] * (3 * (N - 1) + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        w, v = item[i] // offset, item[i] % offset
        for j in range(i + 1):
            for k in range(3 * (N - 1) + 1):
                weight = j * w0 + k
                q, r = (weight - w) // w0, (weight - w) % w0
                if weight < w:
                    dp[i][j][k] = dp[i - 1][j][k]
                elif (weight - w) % w0 > 3 * (N - 1):
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][q][3 * (N - 1)] + v)
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][q][r] + v)
    q, r = W // w0, min(W % w0, 3 * (N - 1))
    print(dp[N][q][r])


if __name__ == "__main__":
    main()
