A, B = map(int,input().split())
A -= 1
B -= 1

grid = [list("#"*100) for _ in range(50)] + [list("."*100) for _ in range(50)]

def fill_white(A):
    for i in range(1,50,2):
        for j in range(0,100,2):
            if A > 0:
                grid[i][j] = "."
                A -= 1
            else:
                return

def fill_black(B):
    for i in range(51,100,2):
        for j in range(0,100,2):
            if B > 0:
                grid[i][j] = "#"
                B -= 1
            else:
                return

fill_white(A)
fill_black(B)

print(100,100)

for line in grid:
    print("".join(line))