x, y = map(int, input().split())
a = [0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
print('Yes' if a[x - 1] == a[y - 1] else 'No')