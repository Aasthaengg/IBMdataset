n, x = map(int, input().split())
a = sorted(map(int, input().split()))
ans = 0
for i in range(n):
    x -= a[i]
    if x < 0:
        break
    if i == n-1:
        if x > 0:
            break
    ans += 1

print(ans)