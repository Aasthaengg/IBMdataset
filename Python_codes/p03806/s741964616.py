import sys
import numpy as np
input = sys.stdin.readline

def main():
    N, Ma, Mb = map(int, input().split())

    INF = int(1e6)
    MAX = (N+1) * 10 + 1
    dp = np.full((MAX, MAX), INF, dtype=np.int64)
    tmp = np.zeros_like(dp)

    dp[0][0] = 0
    for i in range(N):
        a, b, c = map(int, input().split())
        tmp = dp.copy()
        tmp[a:, b:] = np.minimum(tmp[a:, b:], dp[:-a, :-b] + c)
        dp = tmp
    
    ans = INF
    a, b = Ma, Mb
    while a < MAX and b < MAX:
        ans = min(ans, dp[a][b])
        a += Ma
        b += Mb
    
    if ans == INF:
        ans = -1
    
    print(ans)

if __name__ == "__main__":
    main()
