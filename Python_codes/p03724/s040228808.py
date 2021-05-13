N, M = map(int, input().split())

e = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    e[a-1] += 1
    e[b-1] += 1

if all(x % 2 == 0 for x in e):
    print('YES')
else:
    print('NO')
