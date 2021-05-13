# t -> s - > t -> s
sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

ans = []
for i in range(dx):
    ans.append("R")

for j in range(dy):
    ans.append("U")

for i in range(dx):
    ans.append("L")

for j in range(dy):
    ans.append("D")

ans.append("D")

for i in range(dx + 1):
    ans.append("R")

for j in range(dy + 1):
    ans.append("U")

ans.append("L")

ans.append("U")
for i in range(dx + 1):
    ans.append("L")

for j in range(dy + 1):
    ans.append("D")

ans.append("R")

print("".join(ans))
