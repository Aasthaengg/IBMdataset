w, h, n = map(int, input().split())
xya = list(list(map(int, input().split())) for _ in range(n))

left = 0
right = w
down = 0
up = h

for x, y, a in xya:
    if a == 1 and x > left:
        left = x
    if a == 2 and x < right:
        right = x
    if a == 3 and y > down:
        down = y
    if a == 4 and y < up:
        up = y


if right <= left or up <= down:
    ans = 0
else:
    ans = (right - left) * (up - down)

print(ans)
