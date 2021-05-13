a, b, c = tuple(map(int, input().split()))

diff_ab = b - a
diff_cb = c - b
if diff_ab == diff_cb:
    print('YES')
else:
    print('NO')
