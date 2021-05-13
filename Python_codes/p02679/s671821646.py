from math import gcd
MOD = 10**9 + 7
n = int(input())
zero = 0
cnt = dict()
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        zero += 1
        continue
    g = gcd(x, y)
    x //= g
    y //= g
    if y < 0 or (y == 0 and x < 0):
        x *= -1
        y *= -1
    rot_90 = 1 if x <= 0 else 0
    if rot_90:
        x, y = y, -x
    try:
        cnt[(x, y)][rot_90] += 1
    except KeyError:
        cnt[(x, y)] = [int(not rot_90), rot_90]

ans = 1
for s, t in cnt.values():
    now = 1
    now += (pow(2, s, MOD) - 1) % MOD
    now += (pow(2, t, MOD) - 1) % MOD
    ans *= now
ans -= 1
ans += zero
print(ans % MOD)