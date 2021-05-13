n = int(input())
a = []
for i in range(n):
    a.append(int(input()) - 1)

visited = set()

cur = 0
visited.add(0)
ans = 0
while cur != 1:
    if a[cur] not in visited:
        visited.add(a[cur])
        cur = a[cur]
        ans += 1
    else:
        ans = -1
        break

print(ans)
