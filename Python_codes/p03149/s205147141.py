N = map(int, input().split())

S = set([1, 9, 7, 4])
for n in N:
    if n in S:
        S.remove(n)
    else:
        print('NO')
        exit()
else:
    print('YES')
