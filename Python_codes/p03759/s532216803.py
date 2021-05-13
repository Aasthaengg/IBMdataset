a, b, c = map(int, input().split())
left = b - a
right = c - b
if left == right:
    print('YES')
else:
    print('NO')
