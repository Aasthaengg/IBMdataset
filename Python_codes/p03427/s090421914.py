import sys
input = sys.stdin.readline

def main():
    s = input()[:-1]
    n = len(s)
    dp = [[0, 0] for _ in range(n+1)]
    
    for i in range(n):
        key = int(s[n-1-i])
        dp[i+1][0] = dp[i][0] + key
        
        if key > 0:
            dp[i+1][0] = max(dp[i+1][0], dp[i][1] + key - 1)
        
        dp[i+1][1] = max(dp[i][0], dp[i][1]) + 9
    
    print(dp[n][0])
    
    
if __name__ == "__main__":
    main()
