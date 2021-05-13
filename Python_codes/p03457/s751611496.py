N = int(input())
txy = [list(map(int, input().split())) for _ in range(N)]

now_x, now_y = 0, 0
pre_t = 0

for t, x, y in txy:
    walk = abs(now_x - x) + abs(now_y - y)
    if t - pre_t < walk:
        print('No')
        exit()
    if (t-pre_t) % 2 != walk % 2:
        print('No')
        exit()
    now_x = x
    now_y = y
    pre_t = t

print('Yes')