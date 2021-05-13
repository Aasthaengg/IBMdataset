n = int(input())

MOD = 1000000007
whole = 10**n % MOD
bad = (9**n + 9**n - 8**n) % MOD
ans = (whole - bad) % MOD

print(ans)