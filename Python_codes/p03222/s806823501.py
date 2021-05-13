H,W,K = map(int, input().split())

mod = 10**9+7
dp = [["0"]*(W+2) for _ in range(H+1)]
for h in range(H+1):
    dp[h][0] = 0
    dp[h][W+1] = 0
for w in range(W+2):
    dp[0][w] = 0
dp[0][1] = 1

cmb = [1, 2, 3, 5, 8, 13, 21, 34]
def f(h, w):
    if dp[h][w] != "0":
        return dp[h][w]
    dp[h][w] = 0
    dp[h][w] += f(h-1, w-1)*cmb[max(0, w-3)]*cmb[max(0, W-w-1)]
    dp[h][w] += f(h-1, w)*cmb[max(0, w-2)]*cmb[max(0, W-w-1)]
    dp[h][w] += f(h-1, w+1)*cmb[max(0, w-2)]*cmb[max(0, W-w-2)]
    dp[h][w] %= mod
    return dp[h][w]

print(f(H, K))