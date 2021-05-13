n = int(input())
MOD = 1000000007
ret = 10**n - (2 * 9**n - 8**n)
print(ret % MOD)