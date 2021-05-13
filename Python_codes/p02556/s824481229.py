n = int(input())
max_x = max_y = - 5 * 10**9
min_x = min_y = 5 * 10**9
for i in range(n):
    X, Y = map(int, input().split())
    x = X + Y
    y = X - Y
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)
print(max(max_x - min_x, max_y - min_y))
