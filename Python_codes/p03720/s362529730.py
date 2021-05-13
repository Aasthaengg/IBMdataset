N, M  = map(int, input().split())

d = dict.fromkeys(range(1, N+1), 0)

for i in range(M):
    x, y  = map(int, input().split())
    d[x] += 1
    d[y] += 1

for k, v in sorted(d.items()):
    print(v)