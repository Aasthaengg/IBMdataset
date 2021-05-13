n, k = map(int, input().split())

mx = int((n - 1) * (n - 2) / 2)
if mx < k:
    print(-1)
    exit()

ans = []
for i in range(n - 1):
    ans.append([i + 1, n])

edge = []
add = int(mx - k)
for i in range(n - 1):
    for j in range(i):
        edge.append([i + 1, j + 1])

for i in range(add):
    ans.append(edge[i])

print(len(ans))
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
