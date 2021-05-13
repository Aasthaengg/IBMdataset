def main():
    import sys
    input = sys.stdin.readline
    H, W = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    cnt = 0
    ans_list = []
    for y in range(H):
        for x in range(W):
            if grid[y][x] % 2 == 0:
                continue
            if  x + 1 < W:
                cnt += 1
                ans_list.append((y+1, x+1, y+1, x+2))
                grid[y][x+1] += 1
                grid[y][x] -= 1
                continue
            elif y + 1 < H:
                cnt += 1
                ans_list.append((y+1, x+1, y+2, x+1))
                grid[y+1][x] += 1
                grid[y][x] -= 1
                continue

    print(cnt)
    for ans in ans_list:
        print(ans[0], ans[1], ans[2], ans[3])

if __name__ == '__main__':
    main()