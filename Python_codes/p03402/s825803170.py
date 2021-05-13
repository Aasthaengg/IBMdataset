A, B  = map(int, input().split())
grid = []
for h in range(100):
    str = "#"*50 + "."*50
    grid.append(list(str))
cntA = 0
while cntA < A - 1:
    w = cntA % 25
    h = cntA // 25
    grid[2*h][2*w] = "."
    cntA += 1
cntB = 0
while cntB < B - 1:
    w = cntB % 25 + 25
    h = cntB // 25  
    grid[2*h][2*w+1] = "#"
    cntB += 1

print(100,100)
for s in grid:
    print("".join(s))