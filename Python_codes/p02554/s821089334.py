n = int(input())
mod = 10**9+7
r_1,r_2,r_3 = 1,1,1

for i in range(n):
    r_1 = r_1 * 10 % mod
    r_2 = r_2 * 9 % mod
    r_3 = r_3 * 8 % mod

print((r_1-r_2-r_2+r_3)%mod)