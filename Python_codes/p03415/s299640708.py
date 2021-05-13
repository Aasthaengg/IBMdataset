def main():
    grid = [input() for _ in range(3)]
    for i in range(3):
        print(grid[i][i], end="")
    print()


if __name__ == '__main__':
    main()

