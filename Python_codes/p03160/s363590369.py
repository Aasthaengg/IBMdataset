import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush


n = int(input())
H = list(map(int, input().split()))
dp = [INF]*n
dp[0] = 0

def main():
    for i in range(1, n):
        if i == 1:
            dp[i] = dp[i-1] + abs(H[i] - H[i-1])
        else:
            step_1 = dp[i-1] + abs(H[i] - H[i-1])
            step_2 = dp[i-2] + abs(H[i] - H[i-2])
            dp[i] = min(step_1, step_2)
    print(dp[n-1])


if __name__ == '__main__':
    main()
