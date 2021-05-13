A, B = map(int, input().split())

white = '.'
black = '#'
grid = [[black * 100] for i in range(50)] + [[white * 100] for i in range(50)]

for i in range(A-1):
    grid[(i // 50)*2][0] = grid[(i // 50)*2][0][:(i % 50) * 2] + white + grid[(i // 50)*2][0][(i % 50) * 2 + 1:]

for i in range(B-1):
    grid[(i // 50)*2 + 51][0] = grid[(i // 50)*2 + 51][0][:(i % 50) * 2] + black + grid[(i // 50)*2 + 51][0][(i % 50) * 2 + 1:]

print(100, 100)
for g in grid:
    print(g[0])