n  = int(input())
plan = [tuple(map(int, input().split())) for _ in range(n)]

now, now_x, now_y = 0, 0, 0

for t, x, y in plan:
    if abs(x - now_x) + abs(y - now_y) > t - now:
        print('No')
        exit()
    elif ((t - now) - abs(x - now_x) - abs(y - now_y)) % 2 == 1:
        print('No')
        exit()
    now = t
    now_x = x
    now_y = y
print('Yes')