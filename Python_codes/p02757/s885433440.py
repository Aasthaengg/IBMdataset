n, p = map(int, input().split())
s = list(map(int, input()))
if p == 2 or p == 5:
    ans = 0
    for i, digit in enumerate(s):
        if digit % p == 0:
            ans += i + 1
    print(ans)
else:
    ans = 0
    ten_pow_i_mod = 1
    #rev_s_mod = []
    temp_mod = 0
    mod_multiset = [1] + [0] * (p - 1)
    for digit in reversed(s):
        temp_mod += digit * ten_pow_i_mod
        temp_mod %= p
        #rev_s_mod.append(temp_mod)
        ans += mod_multiset[temp_mod]
        mod_multiset[temp_mod] += 1
        ten_pow_i_mod *= 10
        ten_pow_i_mod %= p
    print(ans)