G = [[] for _ in range(4)]
for _ in range(3):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

num = []
for i in range(4):
    num.append(len(G[i]))

cnt = num.count(1)
if cnt < 3:
    print('YES')
else:
    print('NO')