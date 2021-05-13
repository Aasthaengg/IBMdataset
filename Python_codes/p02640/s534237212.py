x, y = map(int, input().split())
print('Yes') if 0 <= (4 * x - y) / 2 <= x and (4 * x - y) % 2 == 0 else print('No')