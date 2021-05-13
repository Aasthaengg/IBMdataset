def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [float('inf')]*n
    dp[0] = 0
    for i in range(n):
        a = h[i]
        for j in range(1, min(k+1, n-i)):
            num = dp[i]+abs(a-h[i+j])
            if num < dp[i+j]:
                dp[i+j] = num
    print(dp[-1])

main()
