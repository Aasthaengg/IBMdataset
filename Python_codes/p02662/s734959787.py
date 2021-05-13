import sys
input = sys.stdin.readline

def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [0]*(s+1)
    dp[0] = 1
    mod = 998244353

    for i in range(n):
        for j in range(s, -1, -1):
            if dp[j] and j + a[i] <= s:
                dp[j+a[i]] += dp[j]
                dp[j+a[i]] %= mod
            dp[j] *= 2
            dp[j] %= mod

    print(dp[s])
    
    
    
if __name__ == "__main__":
    main()
