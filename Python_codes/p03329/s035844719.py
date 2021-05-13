N = int(input())
dp = [None]*(N+1)
a = 1
while a <= N:
    dp[a] = 1
    a *= 6
a = 1
while a <= N:
    dp[a] = 1
    a *= 9

def f(n):
    if dp[n]:
        return dp[n]
    a = 6
    while a <= n:
        a *= 6
    a //= 6
    b = 9
    while b <= n:
        b *= 9
    b //= 9
    ans = min([f(n-a), f(n-b)])+1
    dp[n] = ans
    return ans
print(f(N))