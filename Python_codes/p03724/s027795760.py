N, M = map(int, input().split(' '))
l = [0]*(N-1)
for i in range(M):
    a, b = map(int, input().split(' '))
    if 1 in [a, b]:
        a, b = sorted([a, b])
        l[b-2] += 1
    else:
        l[a - 2] += 1
        l[b - 2] += 1
for i in l:
    if i % 2 != 0:
        print('NO')
        exit()
print('YES')