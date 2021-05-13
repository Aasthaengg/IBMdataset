import sys
#import numpy as np
#from collections import defaultdict
#import math
#from collections import deque

input = sys.stdin.readline



def main():


    N ,K= map(int,input().split())
    H = list(map(int,input().split()))
    H = [0] + H
    dp= [0] *(N+1)
    dp = [10**5] * (N + 1)
    dp[1] = 0

    for i in range(2, N + 1):
        way =[10**10]*(K+2)
        for j in range(1, K+1):
            if j<i:
                way[j]=(dp[i-j]+abs(H[i]-H[i-j]))
        dp[i] = min(way)


    print(dp[N])





if __name__ == "__main__":
    main()