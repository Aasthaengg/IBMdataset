h, w = map(int, input().split())

field = [["@"] * (w + 2)] + [list("@"+input()+"@") for _ in range(h)] + [["@"] * (w + 2)]
direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

flip = {".": "#", "#": "."}

def count_up(i, j):
    que = [(i, j)]
    cnt = {".": 0, "#": 0}
    while que:
        i, j = que.pop()
        now = field[i][j]
        field[i][j] = "@"
        fliped_chip = flip.get(now)
        if fliped_chip is not None:
            cnt[now] += 1
        for d in direction:
            dx, dy = d
            nx, ny = j + dx, i + dy
            next_chip = field[ny][nx]
            if next_chip == fliped_chip:
                que.append((ny, nx))
    return cnt

cnt = [[0] * w for _ in range(h)]
result = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        dot_sharp = count_up(i, j)
        result += (dot_sharp["."] * dot_sharp["#"])
print(result)
#
#
# print("\n".join(map("".join, field)))
#
#
