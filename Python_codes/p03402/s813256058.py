A,B = map(int,input().split())
grid_b = [["#"]*100 for i in range(50)]
grid_w = [["."]*100 for i in range(50)]
for i in range(A-1):
    grid_b[(i//50)*2][(i%50)*2] = "."
for i in range(B-1):
    grid_w[49-(i//50)*2][(i%50)*2] = "#"
grid = grid_b+grid_w
print(100,100)
for y in grid:
    for x in y:
        print(x,end="")
    print()