ns = list(map(int, input().split()))
n = [1, 9, 7, 4]
ok = True
for ni in ns:
    if ni in n:
        n.remove(ni)
    else:
        ok = False

if ok:
    print('YES')
else:
    print('NO')