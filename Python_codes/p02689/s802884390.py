n, m = list(map(int, input().split()))
h = list(map(int, input().split()))
path = [[] for _ in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    if h[a - 1] < h[b - 1]:
        path[a - 1].append(False)
        path[b - 1].append(True)
    elif h[a - 1] == h[b - 1]:
        path[a - 1].append(False)
        path[b - 1].append(False)
    else:
        path[a - 1].append(True)
        path[b - 1].append(False)
ans = 0
for i in path:
    if all(i):
        ans += 1
print(ans)
