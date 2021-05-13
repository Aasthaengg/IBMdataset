w, h, x, y = list(map(int, input().split()))

flag = 0

if x * 2 == w and y * 2 == h:
    flag = 1

print(w * h / 2, flag)