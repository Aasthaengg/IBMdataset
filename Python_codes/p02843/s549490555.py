import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    x = int(input())
    dp = [0 for _ in range(x+106)]
    dp[0] = 1
    for i in range(x):
        if dp[i] == 1:
            for j in range(100, 106):
                dp[i+j] = 1
    print(dp[x])
    return 0

if __name__ == "__main__":
    solve()