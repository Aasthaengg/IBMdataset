from math import gcd

n = int(input())
MOD = 10**9+7
p_map = {}
n_map = {}

p_zero_map = 0
n_zero_map = 0
z_map = 0
for _ in range(n):
    ab = list(map(int, input().split()))
    ab_gcd = gcd(ab[0], ab[1])
    if ab_gcd == 0:
        ab_gcd = 1
    a = ab[0]//ab_gcd
    b = ab[1]//ab_gcd

    if (a > 0 and b > 0) or (a < 0 and b < 0):
        if a < 0:
            a = -a
            b = -b
        key = "{}_{}".format(a, b)
        if key not in p_map:
            p_map[key] = 1
        else:
            p_map[key] += 1
    elif a == 0 and b == 0:
        z_map += 1
    elif a == 0 and b != 0:
        n_zero_map += 1
    elif b == 0 and a != 0:
        p_zero_map += 1
    else:
        if b < 0:
            a = -a
            b = -b
        key = "{}_{}".format(a, b)
        if key not in n_map:
            n_map[key] = 1
        else:
            n_map[key] += 1

ans = 1
for k, v in p_map.items():
    a = int(k.split("_")[0])
    b = int(k.split("_")[1])
    n_num = 0
    key_a = "{}_{}".format(-b, a)
    if key_a in n_map:
        n_num += n_map.pop(key_a)
    res = 0
    res += pow(2, v, MOD)-1
    if n_num > 0:
        res += pow(2, n_num, MOD)-1
    res += 1
    ans *= res
    ans %= MOD

n_num = sum(n_map.values())
if n_num > 0:
    ans *= pow(2, n_num, MOD)
    ans %= MOD

res = 0
if p_zero_map > 0 and n_zero_map > 0:
    res = pow(2, p_zero_map, MOD)-1 + pow(2, n_zero_map, MOD)-1
    res += 1
    res %= MOD
elif p_zero_map > 0 and n_zero_map == 0:
    res = pow(2, p_zero_map, MOD)
elif p_zero_map == 0 and n_zero_map > 0:
    res = pow(2, n_zero_map, MOD)
if res > 0:
    ans *= res
    ans %= MOD


if z_map > 0:
    ans += z_map
ans -= 1
ans %= MOD
print(ans)