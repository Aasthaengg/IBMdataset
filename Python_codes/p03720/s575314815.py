n, m = map(int, input().split())
ll = [[0]] + [ [] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    ll[a].append(b)
    ll[b].append(a)
for l in ll[1:]:
    print(len(l))
