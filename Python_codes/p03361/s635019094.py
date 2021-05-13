# 隣接マスにも黒が存在するか
def check(x, y):
    for i, j in zip(dirx, diry):
        nx = i + x
        ny = j + y
        if nx in range(h) and ny in range(w) and field[nx][ny] == '#':
            return True
    return False


h, w = map(int, input().split())
field = [[c for c in input().strip()] for _ in range(h)]

dirx = [0, 1, 0, -1]
diry = [1, 0, -1, 0]

for i in range(h):
    for j in range(w):
        # そのマスが黒かチェック
        if field[i][j] == '#':
            if not check(i, j):
                print('No')
                exit()
print('Yes')
