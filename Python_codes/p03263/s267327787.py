h, w = map(int, input().split())
a_s = [list(map(int, input().split())) for _ in range(h)]
pm = 1
x = 0
ans = []
car = 0
for y in range(h):
    for _ in range(w - 1):
        if (a_s[y][x] + car) % 2 == 0:
            car = 0
        else:
            car = 1
            ans.append([y + 1, x + 1, y + 1, x + 1 + pm])
        x += pm
    if y != h - 1:
        if (a_s[y][x] + car) % 2 == 0:
            car = 0
        else:
            car = 1
            ans.append([y + 1, x + 1, y + 2, x + 1])
    pm *= -1
print(len(ans))
for row in ans:
    print(*row)