N, M = list(map(int, input().split()))  # N頂点, M個のクエリ

counter = {}
for i in range(1, N+1):
    counter.setdefault(i, 0)

for i in range(M):
    a, b = map(int, input().split())
    counter[a] += 1
    counter[b] += 1

for num in counter.values():
    if num % 2 == 1:
        print('NO')
        exit()

print('YES')
