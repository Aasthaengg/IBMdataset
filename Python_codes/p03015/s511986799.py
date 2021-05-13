l = input()
len_l = len(l)

ans = 0

MOD = 1000000007
def pow_mod(x, y):
    if y == 0: return 1
    ans = 1
    while y > 1:
        if y % 2 != 0: 
            ans *= x
            ans %= MOD
        x *= x
        x %= MOD
        y //= 2
    return ans * x % MOD

keisuu = 1
for i, b in enumerate(l):
  if b == "1":
    ans += (keisuu * pow_mod(3, len_l - i - 1)) % MOD
    ans %= MOD
    keisuu *= 2
    keisuu %= MOD

ans += keisuu
ans %= MOD

print(ans)