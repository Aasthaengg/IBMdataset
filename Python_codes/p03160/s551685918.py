# change minimum
def chmin(a,b):
    return b if a>b else a

# change maximum
def chmax(a,b):
    return b if a<b else a

INF = 1000000000

def main():
    N = int(input())
    h = list(map(int,input().split()))

    # DPテーブル
    dp = [INF]*(10**5+10)

    # 初期条件
    dp[0] = 0

    # roop
    for i in range(1,N):
        dp[i] = chmin(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
        if i>1:
            dp[i] = chmin(dp[i], dp[i-2]+abs(h[i]-h[i-2]))

    print(dp[N-1])

main()