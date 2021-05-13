h, w = list(map(int, input().split()))
grid = []
for i in range(h):
    grid.append(input())

for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            continue

        check = []
        if j != 0:
            check.append([i, j-1])
        if j != w-1:
            check.append([i, j+1])
        if i != 0:
            check.append([i-1, j])
        if i != h-1:
            check.append([i+1, j])

        p = False
        for c in check:
            if grid[c[0]][c[1]] == "#":
                p = True
                break

        if not p:
            print("No")
            exit()

print("Yes")