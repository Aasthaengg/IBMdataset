n,x = map(int, input().split())
a = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    if i != n-1 and a[i] <= x:
        ans += 1
        x -= a[i]
    if i == n-1 and a[i] == x:
        ans += 1
print(ans)