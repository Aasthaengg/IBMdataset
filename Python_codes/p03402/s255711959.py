if __name__ == '__main__':
    A, B = map(int, input().split())
    # A, B = 500, 500
    grid = [["#"] * 50 + ["."] * 50 for _ in range(100)]

    n_locatable_elements = (49 - 1) // 2 + 1
    for i in range(A - 1):
        x = 2 * (i % n_locatable_elements)
        y = 2 * (i // n_locatable_elements) + 1
        grid[y][x] = "."

    for i in range(B - 1):
        x = 2 * (i % n_locatable_elements) + 50 + 1
        y = 2 * (i // n_locatable_elements) + 1
        grid[y][x] = "#"

    print("100 100")
    for row in grid:
        print("".join(row))
