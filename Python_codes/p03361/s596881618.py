def main():
    H, W = map(int, input().split())
    grid = ["." * (W + 2)]
    for _ in range(H):
        grid.append("." + input() + ".")
    grid.append("." * (W + 2))

    DX = (-1, 0, 1, 0, -1, -1, 1, 1)
    DY = (0, 1, 0, -1, -1, 1, -1, 1)
    DX = DX[:4]
    DY = DY[:4]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i][j] == ".":
                continue
            isOK = False
            for dx, dy in zip(DX, DY):
                if grid[i + dx][j + dy] == "#":
                    isOK = True
            if not isOK:
                return "No"

    return "Yes"


if __name__ == "__main__":
    print(main())