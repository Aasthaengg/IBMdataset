N = int(input())
ans = 0
for i in range(N):
    x, y = map(str, input().split())
    if y == 'JPY': ans += float(x)
    else: ans += float(x)*380000
print(ans)
