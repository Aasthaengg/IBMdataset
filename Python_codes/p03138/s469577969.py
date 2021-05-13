#!/usr/bin/env python3
import sys


def solve(N: int, K: int, A: "List[int]"):
    dp = [[-1]*2 for _ in range(45)]
    dp[43][0] = 0
    for i in range(43,-1,-1):
        count = 0 # その桁の1の個数
        for j in range(N):
            if (1 << i & A[j]):
                count += 1
        
        ## 確定から確定
        if dp[i+1][1] >= 0:
            dp[i][1] = max(dp[i+1][1] + max(count,N-count)*(1<<i),dp[i][1])

        if dp[i+1][0] >= 0:
            if K & 1<<i: # Kが１の時
                ## 未確定から未確定
                dp[i][0] = max(dp[i+1][0]+(N-count)*(1<<i),dp[i][0])
                #　未確定から確定
                dp[i][1] = max(dp[i+1][0] + count*(1<<i),dp[i][1])
            else: # Kが0の時
                ## 未確定から未確定
                dp[i][0] = max(dp[i+1][0] + count*(1<<i) ,dp[i][0])
    
    print(max(dp[0][0],dp[0][1]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
