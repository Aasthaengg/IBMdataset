sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

mx = ["R", "L"]
my = ["U", "D"]

ans = mx[0]*dx + my[0]*dy
ans = ans + mx[1]*dx + my[1]*dy
ans = ans + my[1] + mx[0]*(dx + 1) + my[0]*(dy + 1) + mx[1]
ans = ans + my[0] + mx[1]*(dx + 1) + my[1]*(dy + 1) + mx[0]

print(ans)