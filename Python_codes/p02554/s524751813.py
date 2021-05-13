n = int(input())
MOD = 10**9 + 7
if n >= 2:
    ans = pow(10,n,MOD) - 2 * pow(9,n,MOD) + pow(8,n,MOD)
else:
    ans = 0
print(ans%MOD)
