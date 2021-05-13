import sys
sys.setrecursionlimit(10**9)

INF = 10**20
def main():
    N,M = map(int,input().split())

    key = []
    for i in range(M):
        a,_ = map(int,input().split())

        bit = 0
        for c in set(map(int,input().split())):
            bit += 1<<(c-1)

        key.append((a,bit)) # 値段, 開ける宝箱のbit

    dp = [[INF] * (2**N) for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        for j in range(2**N):
            cost,bit = key[i]

            dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            dp[i+1][j|bit] = min(dp[i+1][j|bit],dp[i][j] + cost)

    last = dp[-2][-1]
    print(last if 0 < last < INF else -1)



if __name__ == "__main__":
  main()
