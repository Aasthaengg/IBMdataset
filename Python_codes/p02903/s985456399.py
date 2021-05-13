H, W, A, B = map(int, input().split())

grid_1 = [0] * A + [1] * (W - A)
grid_2 = [1] * A + [0] * (W - A)

for i in range(B):
    print(*grid_1, sep='')
for i in range(H - B):
    print(*grid_2, sep='')