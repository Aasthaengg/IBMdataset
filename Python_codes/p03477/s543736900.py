a, b, c, d = map(int, input().split())
ab = a + b
cd = c + d
print('Left' if ab > cd else 'Right' if ab < cd else 'Balanced')