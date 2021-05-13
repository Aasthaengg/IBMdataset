R,G,B,N = map(int,input().split())
r_max = N // R + 1
g_max = N // G + 1
ans = 0
for r in range(r_max):
    r_num = R * r
    for g in range(g_max):
        g_num = G * g
        b_num = N - r_num - g_num
        if b_num >= 0:
            if b_num % B == 0:
                ans += 1
                # print(r_num,g_num,b_num)
print(ans)
