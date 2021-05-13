N, M = map(int, input().split())  # N頂点, M個のクエリ

counter = [0] * N

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    counter[a] += 1
    counter[b] += 1

flag = True
for i in range(len(counter)):
    if counter[i] % 2 != 0:
        flag = False


if flag:
    print('YES')
else:
    print('NO')
