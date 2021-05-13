n, m, x, y = map(int, input().split())
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))

x_max = max(xl)
y_min = min(yl)
for z in range(x+1, y+1):
    if x_max < z <= y_min:
        print('No War')
        exit()

print('War')
