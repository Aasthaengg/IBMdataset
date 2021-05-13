n, a, b = map(int, input().split())
x = list(map(int, input().split()))

xrui = []
ans = 0
for i in range(n-1):
    xrui.append(x[i + 1] - x[i])

for i in xrui:
    if i * a < b:
        ans += i * a
    else:
        ans += b
print(ans)
