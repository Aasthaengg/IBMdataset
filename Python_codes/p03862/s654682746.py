n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    if a[i] + a[i + 1] <= x:
        continue

    diff = (a[i] + a[i + 1]) - x
    ans += diff

    tmp = min(diff, a[i + 1])
    a[i + 1] -= tmp
    diff -= tmp
    a[i] -= diff
      
print(ans)
