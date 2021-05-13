N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

ans = 1
dp = [0]*3
for a in A:
    ans = ans*dp.count(a) % MOD
    try:
        dp[dp.index(a)] += 1
    except ValueError:
        break
print(ans)
