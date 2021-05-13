n, m = map(int, input().split())
ll = [0] + [ 0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    ll[a] += 1
    ll[b] += 1
for l in ll[1:]:
    print(l)
