# https://atcoder.jp/contests/agc014/tasks/agc014_b

n, m = map(int, input().split())
edges = [0] * n
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append((a, b))

for a, b in ab:
    edges[a - 1] += 1
    edges[b - 1] += 1

for e in edges:
    if e % 2 == 1:
        print('NO')
        break
else:
    print('YES')