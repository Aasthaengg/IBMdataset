from itertools import product
def main():
    h, w, k = map(int, input().split())
    dp = [[0 for j in range(w)] for i in range(h+1)]
    dp[0][0] = 1
    p = []
    for q in product(("-", " "), repeat=w-1):
        f = True
        for j in range(len(q)-1):
            if q[j] == "-" and q[j+1] == "-":
                f = False
        if f:
            p.append(q)
    MOD = 10**9 + 7
    for i in range(1, h+1):
        for q in p:
            for j in range(w):
                if 0 < j and q[j-1] == "-":
                    dp[i][j] += dp[i-1][j-1]
                    dp[i][j] %= MOD
                if j < w-1 and q[j] == "-":
                    dp[i][j] += dp[i-1][j+1]
                    dp[i][j] %= MOD
                if w == 1 or  (0 < j < w-1 and q[j-1] == " " and q[j] == " "):
                    dp[i][j] += dp[i-1][j]
                    dp[i][j] %= MOD
                elif j == 0 and 1 < w and q[j] == " ":
                    dp[i][j] += dp[i-1][j]
                    dp[i][j] %= MOD
                elif j == w-1 and 1 < w and q[j-1] == " ":
                    dp[i][j] += dp[i-1][j]
                    dp[i][j] %= MOD
    print(dp[h][k-1])

if __name__ == "__main__":
    main()