large_p = 10**9 + 7
def main():
    h, w = map(int, input().split())
    grid = [tuple(map(str, input())) for _ in range(h)]
    grid_root = [[0] * w for _ in range(h)]

    # 最もうえの行に「そのセルにいける場合の数」をいれる。右へ進み続けるしかないので１か０。
    flag = 1
    for i1 in range(w):
        if grid[0][i1] == '#':
            flag = 0
        grid_root[0][i1] += flag

    flag = 1
    for i2 in range(h):
        if grid[i2][0] == '#':
            flag = 0
        grid_root[i2][0] += flag
    for j1 in range(1, h):
        for j2 in range(1, w):
            if grid[j1][j2] == '.':
                grid_root[j1][j2] = grid_root[j1-1][j2] + grid_root[j1][j2-1]
    print(grid_root[h-1][w-1] % large_p)

if __name__ == '__main__':
    main()