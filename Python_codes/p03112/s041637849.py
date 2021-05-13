A, B, Q = map(int, input().split())

MY_INF = 10 ** 18

s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]

s = [-MY_INF] + s + [MY_INF]
t = [-MY_INF] + t + [MY_INF]

import bisect

for i, xi in enumerate(x):
    ans = 10 ** 18
    #
    # s -> r
    idx_s = bisect.bisect_left(s, xi)
    #
    s_l = s[idx_s - 1]
    idx_tl = bisect.bisect_left(t, s_l)
    #
    t_ll = t[idx_tl - 1]
    ans_tmp = abs(s_l - xi) + abs(t_ll - s_l)
    ans = min(ans, ans_tmp)
    t_lr = t[idx_tl]
    ans_tmp = abs(s_l - xi) + abs(t_lr - s_l)
    ans = min(ans, ans_tmp)
    #
    s_r = s[idx_s]
    idx_tr = bisect.bisect_left(t, s_r)
    #
    t_rl = t[idx_tr - 1]
    ans_tmp = abs(s_r - xi) + abs(t_rl - s_r)
    ans = min(ans, ans_tmp)
    #
    t_rr = t[idx_tr]
    ans_tmp = abs(s_r - xi) + abs(t_rr - s_r)
    ans = min(ans, ans_tmp)
    #
    # t -> r
    idx_t = bisect.bisect_left(t, xi)
    #
    t_l = t[idx_t - 1]
    idx_sl = bisect.bisect_left(s, t_l)
    #
    s_ll = s[idx_sl - 1]
    ans_tmp = abs(t_l - xi) + abs(s_ll - t_l)
    ans = min(ans, ans_tmp)
    s_lr = s[idx_sl]
    ans_tmp = abs(t_l - xi) + abs(s_lr - t_l)
    ans = min(ans, ans_tmp)
    #
    t_r = t[idx_t]
    idx_sr = bisect.bisect_left(s, t_r)
    #
    s_rl = s[idx_sr - 1]
    ans_tmp = abs(t_r - xi) + abs(s_rl - t_r)
    ans = min(ans, ans_tmp)
    #
    s_rr = s[idx_sr]
    ans_tmp = abs(t_r - xi) + abs(s_rr - t_r)
    ans = min(ans, ans_tmp)
    #
    print(ans)
