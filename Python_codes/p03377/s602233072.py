A, B, X = map(int, input().split())

need = X - A

if need >= 0:
    if need <= B:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
