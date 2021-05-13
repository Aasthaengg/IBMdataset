n = int(input())

now_t = 0
now_xy = 0
for i in range(n):
    t, x, y = map(int, input().split())
    baf = 0
    if not abs((x+y) - now_xy) == t - baf*2 - now_t:
        while t-baf*2-now_t >= 2:
            baf += 1
            if abs((x+y) - now_xy) == t - baf*2 - now_t:
                break
        else:
            print("No")
            exit()
    now_t = t
    now_xy = x + y
print("Yes")
