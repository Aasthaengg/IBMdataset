n, k = map(int, input().split())
ans = 0
for i in range(n):
    if i + k - 1 < n:
        ans += 1
print(ans)
