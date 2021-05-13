def check(i, j, c):
    if grid[i - 1][j - 1] != c and grid[i][j - 1] != c and grid[i + 1][j - 1] != c and grid[i - 1][j] != c and grid[i + 1][j] != c and grid[i - 1][j + 1] != c and grid[i][j + 1] != c and grid[i + 1][j + 1] != c:
        return True
    else:
        return False

def change(N, c):
    k = 0
    if c == "#":
        k = 50
    for i in range(1 + k, 49 + k):
        for j in range(1, 99):
            if check(i, j, c):
                grid[i][j] = c
                N -= 1
            if N == 1:
                break
        if N == 1:
            break

A, B = map(int, input().split())
grid = [["#" for i in range(100)] for i in range(50)] + [["." for i in range(100)] for i in range(50)]
print(100, 100)
if A > 1:
    change(A, ".")
if B > 1:
    change(B, "#")
for g in grid:
    print("".join(g))