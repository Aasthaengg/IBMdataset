import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    a = [0] * n
    MOD = 10 ** 9 + 7
    for _ in range(m):
        a[int(input())] = 1
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(n):
        dp[i] %= MOD
        if a[i]:
            dp[i] = 0
        if i + 1 <= n:
            dp[i+1] += dp[i]
        if i + 2 <= n:
            dp[i+2] += dp[i]
    print(dp[-1]%MOD)
    
if __name__ == '__main__':
    main()