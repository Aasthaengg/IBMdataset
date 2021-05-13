n = int(input())

now_time = 0
now_x = 0
now_y = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    xy_diff = abs(x - now_x) + abs(y - now_y)

    if t - now_time < xy_diff:
        print("No")
        exit()
    if (t - now_time) % 2 == 0:
        if xy_diff % 2 != 0:
            print("No")
            exit()
        else:
            now_time = t
            now_x = x
            now_y = y
    else:
        if xy_diff % 2 != 1:
            print("No")
            exit()
        else:
            now_time = t
            now_x = x
            now_y = y

print("Yes")
