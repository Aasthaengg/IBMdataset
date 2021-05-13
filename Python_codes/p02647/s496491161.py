n, k = map(int, input().split())
lst = list(map(int, input().split()))

if n**(1/2) <= k:
    lst = [n for _ in range(n)]
    print(*lst)
else:
    for _ in range(k):
        ans = 0
        dp = [0] * (n + 1)
        for _ in range(n):  
            mx = max(0,_ - lst[_])
            mn = min(n, _ + lst[_] +1)
            dp[mx] += 1
            dp[mn] -= 1
        
        for _ in range(n):
            ans = ans + dp[_]
            lst[_] = ans

    print(*lst[:n])