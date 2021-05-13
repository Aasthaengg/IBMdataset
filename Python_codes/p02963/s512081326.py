s = int(input())

ax = 10 ** 9
by = 10 ** 9

bx_x_ay = ax * by - s

q, r = divmod(bx_x_ay, 10 ** 9)
by -= q
bx = 1
ay = r

ans = (0, 0) + (ax, ay) + (bx, by)
print(*ans)

# print(abs(ax * by - bx * ay))

# 三角形の面積 := s / 2 = abs(a.x * b.y - b.x * a.y) / 2
# 三角形の面積 := s / 2 = abs((a.x - c.x) * (b.y - a.y) - (a.x - b.x) * (c.y - a.y)) / 2
