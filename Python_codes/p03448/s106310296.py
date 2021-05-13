import sys
input = sys.stdin.readline
import math


def read():
    A = int(input().strip())
    B = int(input().strip())
    C = int(input().strip())
    X = int(input().strip())
    return A, B, C, X

def solve(A, B, C, X, XMAX=20001):
    dp = [[0 for j in range(XMAX)] for i in range(4)]
    dp[0][0] = 1
    for i, (v, c) in enumerate(zip([500, 100, 50], [A, B, C])):
        for x in range(XMAX):
            for j in range(c+1):
                if x - j * v >= 0:
                    dp[i+1][x] += dp[i][x - j * v]
    return dp[3][X]


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
