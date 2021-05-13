s=input()
ans = 0
p_n = 0; g_n = 0
for s_i in s:
    if s_i == "g":
        if p_n < g_n:
            ans += 1
            p_n += 1
        else:
            g_n += 1
    else:
        if p_n < g_n:
            p_n += 1
        else:
            g_n += 1
            ans -= 1
print(ans)
