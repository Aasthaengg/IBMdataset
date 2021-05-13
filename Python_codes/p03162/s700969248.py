import sys
#import numpy as np
#from collections import defaultdict
import math
#from collections import deque

input = sys.stdin.readline



def main():


    n = int(input())

    dp = [0]*n
    dp[0] = list(map(int,input().split()))

    for i in range(1,n):
        dp[i] = list(map(int,input().split()))
        dp[i][0] += max(dp[i-1][1],dp[i-1][2])
        dp[i][1] += max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] += max(dp[i - 1][0], dp[i - 1][1])
    print(max(dp[n-1]))


if __name__ == "__main__":
    main()