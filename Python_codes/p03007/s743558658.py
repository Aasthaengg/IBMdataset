n = int(input())
a = sorted(map(int, input().split()))
ans = []
for i in range(1, n - 1):
    # +
    if a[i] < 0:
        ans.append([a[-1], a[i]])
        a[-1] -= a[i]
    # -
    else:
        ans.append([a[0], a[i]])
        a[0] -= a[i]
ans.append([a[-1], a[0]])
print(a[-1] - a[0])
for x, y in ans:
    print(x, y)
