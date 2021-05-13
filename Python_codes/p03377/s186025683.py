A, B, X = map(int, input().split())
X -= A
if X < 0:
    print('NO')
elif X <= B:
    print('YES')
else:
    print('NO')