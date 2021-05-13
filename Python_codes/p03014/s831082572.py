h, w = list(map(int, raw_input().split()))
grid = [raw_input() for _ in range(h)]

cnt = [[0]*w for _ in range(h)]

yStarts = [-1] * w
yStrks = [0] * w

for y in range(h):
    xStart = -1
    xStrk = 0

    for x in range(w):
        if grid[y][x] == ".":
            if xStart == -1:
                xStart = x
            xStrk += 1

            if yStarts[x] == -1:
                yStarts[x] = y
            yStrks[x] += 1

        if grid[y][x] == "#" or x == w-1:
            if xStart != -1:
                xEnd = x if grid[y][x] == "." else x-1

                for x2 in range(xStart, xEnd+1):
                    cnt[y][x2] += (xEnd-xStart)+1

            xStart = -1
            xStrk = 0

        if grid[y][x] == "#" or y == h-1:
            if yStarts[x] != -1:
                yEnd = y if grid[y][x] == "." else y-1

                for y2 in range(yStarts[x], yEnd+1):
                    cnt[y2][x] += (yEnd-yStarts[x])+1

            yStarts[x] = -1
            yStrks[x] = 0

ans = 0
for y in range(h):
    for x in range(w):
        ans = max(ans, cnt[y][x]-1)

print(ans)
