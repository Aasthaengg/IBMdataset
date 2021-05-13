R, G, B, N = map(int, input().split())
MAX_R = N // R + 1
MAX_G = N // G + 1
ans = 0
for i in range(MAX_R):
    for j in range(MAX_G):
        b_cnt = N - R * i - G * j
        if b_cnt >= 0 and b_cnt % B == 0:
            ans += 1

print(ans)
