h, w = [int(x) for x in input().split()]
s_list = [input() for _ in range(h)]

def count_bomb_num(i, j):
    bomb_num = 0
    for k in range(-1, 2):
        if j == 0 and k == -1:
            continue
        if j == w - 1 and k == 1:
            continue
        if s_list[i][j + k] == "#":
            bomb_num += 1
    return bomb_num

count_list = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i == 0:
            count_list[i][j] = count_bomb_num(i, j)
        if i < h - 1:
            count_list[i + 1][j] = count_bomb_num(i + 1, j)
        
        if s_list[i][j] == "#":
            print("#", end="")
        else:
            bomb_num = count_list[i][j]
            if i > 0:
                bomb_num += count_list[i - 1][j]
            if i < h - 1:
                bomb_num += count_list[i + 1][j]
            print(bomb_num, end="")
    print()