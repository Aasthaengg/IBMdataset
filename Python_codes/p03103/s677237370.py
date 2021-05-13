n, m = map(int, input().split())
AB = []
for i in range(n):
    a,b = map(int, input().split())
    AB.append((a, b))
AB.sort()

ans = 0
for i in range(m):
    a, b = AB[i]
    if b >= m:
        ans += a*m
        break
    else:
        ans += a*b
        m -= b
print(ans)
