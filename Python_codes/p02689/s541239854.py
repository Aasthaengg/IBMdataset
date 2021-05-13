n, m = map(int, input().split())
h = list(map(int, input().split()))

d = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)

ans = 0
for i in range(n):
    flg = True
    for j in d[i]:
        if h[i] <= h[j]:
            flg = False
            break
    if flg:
        ans += 1

print(ans)