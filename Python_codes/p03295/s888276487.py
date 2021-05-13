n, m = map(int, input().split())
lst = []
for i in range(m):
    ai, bi = map(int, input().split())
    ai, bi = ai-1, bi-1
    lst.append([ai, bi])

lst.sort(key=lambda x: x[1])

ans = 1
kiru = lst[0][1]
for i in range(1, m):
    if lst[i][0] >= kiru:
        ans += 1
        kiru = lst[i][1]

print(ans)