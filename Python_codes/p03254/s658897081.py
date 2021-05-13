n, x = [int(_) for _ in input().split()]
a = sorted([int(_) for _ in input().split()])
ans = 0
for i in range(n):
    x -= a[i]
    if x < 0:
        break
    else:
        ans += 1
print(ans - 1 if x > 0 else ans)