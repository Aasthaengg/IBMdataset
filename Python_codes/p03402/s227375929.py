A,B = map(int,input().split())
grid = [[0]*50+[1]*50 for _ in range(100)]
point = 0
for a in range(A-1):
    grid[point%100][int(point/100)*2] = 1
    point += 2
point = 0
for b in range(B-1):
    grid[point%100][99-int(point/100)*2] = 0
    point  += 2
print(100,100)
for gg in grid:
    temp = ""
    for g in gg:
        temp += "#" if g == 0 else "."
    print(temp)