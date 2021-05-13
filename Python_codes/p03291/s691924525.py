s=input()
all_hatena = s.count('?')

a_cnt = 0
ab_cnt = 0
hatena_cnt = 0
ans = 0

MOD = 10**9+7
for si in s:
    if si == 'A':
        a_cnt += 1
    elif si == 'B':
        ab_cnt += a_cnt*pow(3,all_hatena,MOD)
        if all_hatena >= 1: ab_cnt += hatena_cnt*pow(3,all_hatena-1,MOD)
    elif si == 'C':
        ans += ab_cnt
    else:
        ans += ab_cnt*333333336 # modinv(3,MOD)
        ab_cnt += a_cnt*pow(3,all_hatena-1,MOD)
        if all_hatena >= 2: ab_cnt += hatena_cnt*pow(3,all_hatena-2,MOD)
        hatena_cnt += 1
    ab_cnt%=MOD
    ans%=MOD
print(ans)