#!/usr/bin/env python3
import sys, math, fractions, itertools

MOD = 1000000007  # type: int

def solve(h: int, w: int, k: int):
    wc = [1] * 9

    for i in range(2, 9):
        wc[i] = wc[i-1] + wc[i-2]

    dp = [0] * (w+2)
    dp[1] = 1
    for i in range(h):
        tmp = [0] * (w+2)
        for j in range(1, w+1):
            tmp[j] = dp[j] * wc[j-1] * wc[w-j]
            if j > 1:
                tmp[j] += dp[j-1] * wc[j-2] * wc[w-j]
            if j < w:
                tmp[j] += dp[j+1] * wc[j-1] * wc[w-j-1]
            tmp[j] = tmp[j] % MOD
        dp = tmp
    print(dp[k])

    return


# Generated by 1.1.4 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(H, W, K)

if __name__ == '__main__':
    main()
