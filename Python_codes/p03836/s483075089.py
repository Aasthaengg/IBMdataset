sx, sy, tx, ty = map(int, input().split())

dx = abs(tx - sx)
dy = abs(ty - sy)

s = ['U'] * dy + ['R'] * dx + ['U'] + ['L'] * (dx+1) + ['D'] * (dy+1) + ['R'] + ['R'] * dx + ['U'] * dy + ['R'] + ['D'] * (dy+1) + ['L'] * (dx + 1) + ['U']

print("".join(s))
