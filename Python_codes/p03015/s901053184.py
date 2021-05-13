#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(L: str):
    N = len(L)

    #dp[i][j] = i桁めまでみたとき、j=0のとき、L以下であることが確定していない、j=1確定している
    dp = [[0]*2 for _ in range(N+1)]
    dp[0][0] = 1    

    for i in range(N):
        dp[i+1][1] += dp[i][1]*3
        if L[i] == "1":
            dp[i+1][1] += dp[i][0]
            dp[i+1][0] += dp[i][0]*2
        else: # 0
            #0のときは確定することはない
            dp[i+1][0] += dp[i][0]
        dp[i+1][0]%=MOD
        dp[i+1][1]%=MOD

    print((dp[N][0]+dp[N][1])%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = next(tokens)
    solve(L)

if __name__ == '__main__':
    main()
