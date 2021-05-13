n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)

#print(g)
for i in range(n):
    if len(g[i])%2 == 1:
        print('NO')
        exit()
else:
    print('YES')
