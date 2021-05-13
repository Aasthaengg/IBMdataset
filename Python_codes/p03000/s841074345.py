n, x = map(int, input().split())
l = list(map(int, input().split()))

d = 0
ans = 0
for i in range(n + 1):
    if d <= x:
        ans += 1
        if i == n:
            break
        d += l[i]
    else:
        break
print(ans)
