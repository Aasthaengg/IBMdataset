k, s = map(int, input().split())

ans = 0
for q in range(k + 1):
    for w in range(k + 1):
        if 0 <= (s - q - w) <= k:
            ans += 1
print(ans)