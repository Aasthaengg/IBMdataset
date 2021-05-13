#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    # dp[1]: flipped
    dp = [[float('inf')] * N for _ in range(2)]
    dp[0][0] = A[0]
    dp[1][0] = -A[0]
    for i, a in enumerate(A[1:], 1):
        dp[0][i] = max(dp[0][i-1]+a, dp[1][i-1]-a)
        dp[1][i] = max(dp[0][i-1]-a, dp[1][i-1]+a)
    return max(dp[0][N-2]+A[-1], dp[1][N-2]-A[-1])


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, A))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()