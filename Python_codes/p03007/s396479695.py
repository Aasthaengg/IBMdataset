N = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
if a[0] > 0:
    x = a[0]
    for i in range(1, N - 1):
        ans.append((x, a[i]))
        x -= a[i]
    ans.append((a[-1], x))
    x = a[-1] - x
elif a[-1] < 0:
    x = a[-1]
    for i in range(N - 2, -1, -1):
        ans.append((x, a[i]))
        x -= a[i]
else:
    x = a[0]
    for i in range(1, N - 1):
        if a[i] >= 0:
            ans.append((x, a[i]))
            x -= a[i]
    ans.append((a[-1], x))
    x = a[-1] - x
    for i in range(1, N - 1):
        if a[i] < 0:
            ans.append((x, a[i]))
            x -= a[i]

print(x)
for a, b in ans:
    print(a, b)