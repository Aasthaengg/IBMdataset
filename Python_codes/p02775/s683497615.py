#!/usr/bin/env python3
import sys
# sys.setrecursionlimit(10000000)
# INF = 1<<32

def solve(N: "List[int]"):
    # N=36を考える
    # l = list(map(int, list(str(N))))
    dp = 0,1
    for i in N:
        # a = f(3), f(36)
        a = min(dp[0]+i, dp[1]+10-i)
        # b = f(4), f(40)
        b = min(dp[0]+i+1, dp[1]+10-(i+1))
        dp = a, b

    print(dp[0])
    return



def main():
    stdin = open(0)
    N = [int(x) for x in stdin.read().rstrip()]
    solve(N)

if __name__ == '__main__':
    main()
