# input here
_INPUT = """\
127
"""
"""
K = int(input())
H, W, K = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for i in range(N)]
p = tuple(map(int,input().split()))
"""
def main():
    N = int(input())

    dp = [float('inf')] * (N+1)
    dp[0] = 0
    a,b,c = 1,6,9

    for i in range(N+1):
        if i >= b*6:
            b *= 6
        if i >= c*9:
            c *= 9
        if i < b:
            dp[i] = i
        elif i < c:
             dp[i] = min(dp[i-1]+1, dp[i-b]+1)
        else:
            dp[i] = min(dp[i-1]+1,dp[i-b]+1,dp[i-c]+1)
    
    print(dp[N])
            
            
if __name__ == '__main__':
    import io
    import sys
    import math
    import itertools
    from collections import deque

    # sys.stdin = io.StringIO(_INPUT)
    main()