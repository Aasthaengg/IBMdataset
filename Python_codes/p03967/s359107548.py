S = input()

g_cnt, p_cnt = 0, 0
ans = 0
for s in S:
    if p_cnt < g_cnt:
        if s == "g":
            p_cnt += 1
            ans += 1
        elif s == "p":
            p_cnt += 1
    else:
        if s == "g":
            g_cnt += 1
        elif s == "p":
            g_cnt += 1
            ans -= 1
print(ans)