s = input()
n = len(s)
MOD = 10**9+7

ans = 1
p3 = 1
for i in range(-1, -n-1, -1):
    if s[i] == '1':
        ans = ((ans * 2) % MOD + p3) % MOD
    p3 = (p3 * 3) % MOD
print(ans)