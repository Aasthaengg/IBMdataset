n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

d = {}
for i in range(m):
    d[i+1] = 0

for i in a:
    for j in i[1:]:
        d[j] += 1
ans = 0
for i in d.values():
    if i == n:
        ans += 1
print(ans)