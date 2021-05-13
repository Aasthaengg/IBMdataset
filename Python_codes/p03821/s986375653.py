n = int(input())
a = []
b = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

ans = 0
for i in range(n-1, -1, -1):
    a[i] += ans
    mod = a[i] % b[i]
    if mod != 0:
        if a[i] > b[i]:
            ans += b[i] - mod
        else:
            ans += b[i] - a[i]

print(ans)
