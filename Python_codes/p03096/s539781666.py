INF = 10 ** 9
MOD = 10 ** 9 + 7
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  copy import deepcopy
from bisect import bisect_left

def main():
    n = int(input())
    C = [int(input()) for _ in range(n)]

    dic = {i:0 for i in set(C)}
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if i > 0 and C[i] == C[i - 1]:
            dp[i + 1] = dp[i]
            continue
        else:
            dp[i + 1] = (dp[i] + dic[C[i]])%MOD
            dic[C[i]] += dp[i]
            dic[C[i]] %= MOD
    print(dp[-1]%MOD)
    
if __name__ == '__main__':
    main() 