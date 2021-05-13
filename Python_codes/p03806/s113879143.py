# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
INF = 10**10
def main(N, Ma, Mb, ABC):
    MX = 10 * N
    dp = [[[INF] * (MX + 1) for _ in range(MX + 1)] for __ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        ni = i + 1
        ma, mb, mc = ABC[i]
        for na in range(MX + 1):
            a = na - ma
            for nb in range(MX + 1):
                b = nb - mb
                dp[ni][na][nb] = dp[i][na][nb]
                if a >= 0 and b >= 0:
                    dp[ni][na][nb] = min(dp[ni][na][nb], dp[i][a][b] + mc)

    ans = INF
    for a in range(MX + 1):
        for b in range(MX + 1):
            if a == 0 and b == 0: continue
            if a * Mb == b * Ma:
                ans = min(ans, dp[N][a][b])
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, Ma, Mb = map(int, input().split())
    ABC = [tuple(map(int, input().split())) for _ in range(N)]
    main(N, Ma, Mb, ABC)
