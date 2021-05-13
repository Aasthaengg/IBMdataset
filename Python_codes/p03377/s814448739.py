A, B, X = map(int, input().split())
if X - A >= 0 and X <= A + B:
    print('YES')
else:
    print('NO')
