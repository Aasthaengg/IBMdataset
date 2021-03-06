#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, K: int):
    num_gcd = {}
    for k in range(K, 0, -1):
        num_select = K // k
        num_gcd_k = pow(num_select, N, MOD)
        for multiple in range(2, num_select+1):
            num_gcd_k -= num_gcd[k * multiple]
        num_gcd[k] = num_gcd_k

    result = 0
    for k in range(1, K+1):
        result += (k * num_gcd[k]) % MOD
    print(result % MOD)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
