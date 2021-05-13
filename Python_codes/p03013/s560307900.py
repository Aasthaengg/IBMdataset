# input here
_INPUT = """\
10 2
4
5
"""
"""
K = int(input())
H, W, K = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for i in range(N)]
p = tuple(map(int,input().split()))
"""
def main():
    N, M = map(int, input().split())
    a = set([int(input()) for i in range(M)])
    inf = 10**9+7

    #動的計画法問題
    dp = [0] * (N+1)
    dp[0] = 1
    if 1 not in a:
        dp[1] = 1
    else:
        dp[1] = 0

    for i in range(2,N+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        
        dp[i] %= inf

    print(dp[N]) 

     
if __name__ == '__main__':
    import io
    import sys
    import math
    import itertools
    from collections import deque

    # sys.stdin = io.StringIO(_INPUT)
    main()