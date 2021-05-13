A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(M):
    x, y, c = map(int, input().split())
    if i == 0:
        ans = a[x - 1] + b[y - 1] - c
        continue
    ans = min(ans, a[x - 1] + b[y - 1] - c)

a.sort()
b.sort()
ans = min(ans,a[0] + b[0])
print(ans)