a, b, c = input().rstrip().split()
if a[-1] == b[0] and b[-1] == c[0]:
    print('YES')
else:
    print('NO')