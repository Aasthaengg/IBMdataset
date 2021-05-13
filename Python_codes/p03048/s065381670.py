r, g, b, n = map(int, input().split())
ans = 0
for i in range(0, n+1, r):
    for j in range(i, n+1, g):
        if (n-j) % b == 0:
            ans += 1
print(ans)
