A, B = map(int, input().split())

grid = [["." for _ in range(100)] for _ in range(100)]

# 上半分（50*100）を黒で、下半分(50*100)を白で埋める
for r in range(50):
    for c in range(100):
        grid[r][c] = "#"

# 上の(49*100)において、A-1マスを白に塗り替える
cnt_w = 1
for r in range(0, 49, 2):
    for c in range(100):
        if cnt_w < A:
            if c % 2 == 0:
                grid[r][c] = "."
                cnt_w += 1
        else:
            break

# 下の(49*100)において、B-1マスを黒に塗り替える
cnt_b = 1
for r in range(51, 100, 2):
    for c in range(100):
        if cnt_b < B:
            if c % 2 == 0:
                grid[r][c] = "#"
                cnt_b += 1
        else:
            break

print(100, 100)
for r in range(100):
    print("".join(grid[r]))
