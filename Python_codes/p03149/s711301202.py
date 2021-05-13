def resolve():
    l = set(map(int, input().split()))
    if l == {1, 7, 9, 4}:
        print('YES')
    else:
        print('NO')
resolve()