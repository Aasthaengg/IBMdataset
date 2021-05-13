import sys
#input = sys.stdin.buffer.readline

def main():
    N = int(input())
    S = [list(str(input())) for _ in range(2)]
    dp = [0 for _ in range(N)]
    MOD = 10**9+7
    
    if S[0][0] == S[1][0]:
        dp[0] = 3
        for i in range(1,N):
            if S[0][i-1] != S[0][i]:
                if S[0][i-1] == S[1][i-1]:
                    dp[i] = (dp[i-1]*2)%MOD
                else:
                    if S[0][i] == S[1][i]:
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = (dp[i-1]*3)%MOD
            else:
                dp[i] = dp[i-1]
    else:
        dp[0] = dp[1] = 6
        for i in range(2,N):
            if S[0][i-1] != S[0][i]:
                if S[0][i-1] == S[1][i-1]:
                    dp[i] = (dp[i-1]*2)%MOD
                else:
                    if S[0][i] == S[1][i]:
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = (dp[i-1]*3)%MOD
            else:
                dp[i] = dp[i-1]
                
    print(dp[-1]%MOD)

if __name__ == "__main__":
    main()
