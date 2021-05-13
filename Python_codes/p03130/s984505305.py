L = [0] * 5
for _ in range(3):
    a, b = map(int,input().split())
    L[a] += 1
    L[b] += 1

if 3 in L:
    print('NO')
else:
    print('YES')