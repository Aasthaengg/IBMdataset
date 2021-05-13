n, x = map(int, input().split())
l = sorted(list(map(int, input().split())))

ans = 0
for i in range(n-1):
    if l[i] <= x:
        x -= l[i]
        ans += 1
else:
    if l[-1] == x:
        ans += 1
print(ans)