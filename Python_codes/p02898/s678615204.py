n, k = map(int, input().split())
h = list(map(int, input().split()))
ans = 0
for high in h:
    if high >= k:
        ans = ans + 1
print(ans)