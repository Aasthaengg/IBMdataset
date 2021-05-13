import sys
from math import gcd
from itertools import combinations


def main():
    input = sys.stdin.buffer.readline
    k = int(input())
    dp = [1]*(k+1)
    for i in range(2, k+1):
        dp[i] = dp[i-1]+i
        for e in combinations(range(1, i), 2):
            dp[i] += 6*gcd(gcd(e[0], e[1]), i)
        for j in range(1, i):
            dp[i] += 6*gcd(i, j)
    print(dp[k])


if __name__ == '__main__':
    main()
