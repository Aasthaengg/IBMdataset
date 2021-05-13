def main():
    grid = [list(map(int, input().split())) for _ in range(3)]

    if grid[0][0] == (grid[0][2] + grid[2][0]) - grid[2][2] and grid[1][1] == (grid[0][1] + grid[1][0]) - grid[0][0] and grid[2][2] == (grid[1][2]+grid[2][1]) - grid[1][1]:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
