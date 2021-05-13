a, b = map(int, input().split())
ans = 0
for i in range(1, a):
    for j in range(1, 32):
        if i == j:
            ans += 1
for k in range(1, b + 1):
    if k == a:
        ans += 1
print(ans)
