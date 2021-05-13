N, M = map(int, input().split())
ab = []
for _ in range(M):
    ab.append(tuple(map(int, input().split())))

bucket = [0] * N
for el in ab:
    a, b = el
    bucket[a - 1] += 1
    bucket[b - 1] += 1
if all([x % 2 == 0 for x in bucket]):
    print('YES')
else:
    print('NO')