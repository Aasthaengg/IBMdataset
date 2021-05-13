n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
is_neighbor = [[True] * n for i in range(n)]

f = True
for i in range(n):
    if not f: break
    for s in range(n):
        if not f: break
        for t in range(n):
            if a[s][t] > a[s][i] + a[i][t]:
                f = False
                break
            elif i == s or i == t: continue
            elif a[s][t] == a[s][i] + a[i][t]:
                is_neighbor[s][t] = False
if f:
    ans = 0
    for i in range(n):
        for j in range(n):
            if is_neighbor[i][j]:
                ans+=a[i][j]
    print(ans//2)
else:
    print(-1)