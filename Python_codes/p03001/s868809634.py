W, H, x, y = list(map(int, input().split()))

area = W * H / 2

checker = 0

if(x == W / 2 and y == H / 2):
    checker = 1

print(area, checker)