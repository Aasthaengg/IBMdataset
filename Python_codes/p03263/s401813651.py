h, w = map(int, input().split())

a = []

for i in range(h):
    a.append(list(map(int, input().split())))

d = 1
x = 0

moving = 0

ans = []

st = []

prev_y = 0
prev_x = 0

for y in range(h):
    while 0 <= x < w:
        if moving == 0 and a[y][x] % 2 != 0:
            moving = 1
        elif moving == 1 and a[y][x] % 2 != 0:
            st.append(' '.join(list(map(str, [prev_y+1, prev_x+1, y+1, x+1]))))
            moving = 0
            ans += st
            st = []
        elif moving == 1 and a[y][x] % 2 == 0:
            st.append(' '.join(list(map(str, [prev_y+1, prev_x+1, y+1, x+1]))))
        prev_y = y
        prev_x = x

        x += d

    d *= (-1)
    x += d

print(len(ans))

for i in range(len(ans)):
    print(ans[i])
