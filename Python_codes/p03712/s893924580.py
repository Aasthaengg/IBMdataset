h, w = map(int, input().split())
htop = '#' * (w+2)
grid = [htop]
for _ in range(h):
    grid.append('#' + str(input()) + '#')
else:
    grid.append(htop)
print(*grid, sep='\n')