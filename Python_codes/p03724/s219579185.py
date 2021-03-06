N, M = map(int, input().split(' '))
count = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split(' '))
    count[a - 1] += 1
    count[b - 1] += 1

if all([c % 2 == 0 for c in count]):
    print('YES')
else:
    print('NO')