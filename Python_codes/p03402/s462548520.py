nim, mike = map(int, input().split())

g = [["#"]*100 for _ in range(50)] + [["."]*100 for _ in range(50)]

for i in range(nim-1):
    x, y = (i%50)*2, (i//50)*2
    g[y][x] = "."
for i in range(mike-1):
    x, y = (i%50)*2, 51+(i//50)*2
    g[y][x] = "#"

print(100, 100)
for g_i in g:
    print("".join(g_i))
