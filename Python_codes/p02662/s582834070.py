import sys
input = sys.stdin.buffer.readline
import copy

def main():
    N,S = map(int,input().split())
    a = list(map(int,input().split()))
    MOD = 998244353

    dp = [0]*(S+1)
    dp[0] = 1
    for num in a:
        dp2 = dp.copy()
        for i in range(S-num+1):
            dp2[num+i] += dp[i]
        for i in range(S+1):
            dp[i] += dp2[i]
            dp[i] %= MOD
    
    print(dp[-1]%MOD)

if __name__ == "__main__":
    main()