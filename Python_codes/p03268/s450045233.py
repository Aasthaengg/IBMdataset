N , K = map(int, input().split())

mod_0_num = N//K

ans_mod_0 = mod_0_num**3
ans_mod_K = 0
if K%2 == 0:
    mod_K_num = (2*N-K)//(2*K) + 1
    ans_mod_K = mod_K_num**3

ans = ans_mod_0 + ans_mod_K
print(ans)