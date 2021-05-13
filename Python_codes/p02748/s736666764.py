a, b, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc = []
for _ in range(m):
    xyc.append(list(map(int, input().split())))
ans = min(a) + min(b)

for x, y, c in xyc:
    tmp = a[x - 1] + b[y - 1] - c
    ans = min(ans, tmp)
print(ans)