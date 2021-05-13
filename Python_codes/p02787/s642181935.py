#from pprint import pprint
#from collections import deque
#from collections import defaultdict
#from collections import Counter
#from copy import deepcopy
#from itertools
#import sys 
#sys.setrecursionlimit(N) #N回まで再起を許可する。
 
# = map(int,input().split())
 
# = list(map(int,input().split()))
 
# = [list(map(int,input().split())) for _ in range(XXXX)]
from sys import stdin


def main():
    input = stdin.readline
    
    h,n = map(int,input().split())
    
    ab= [list(map(int,input().split())) for _ in range(n)]
    
    dp = [[100000001 for _ in range(h+1)] for _ in range(n+1)]
    #dp[i][j]はi番目のものを選んだ時かつダメージ送料がjだったときの最小MP、
    
    
    for i in range(1,n+1):
        dp[i][0] = 0
        for j in range(h+1):
            a = ab[i-1][0]
            b = ab[i-1][1]
            dp[i][j] = min(dp[i][j],dp[i-1][j])
            if j+a <= h:
                dp[i][j+a] = min(dp[i][j] + b, dp[i-1][j+a], dp[i][j+a])
            elif j+a > h:
                dp[i][h] = min(dp[i][j] + b, dp[i-1][h], dp[i][h])

    
    print(dp[-1][-1])

if __name__ == "__main__":
    main()