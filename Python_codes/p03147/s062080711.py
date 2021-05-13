n = int(input())
h = list(map(int, input().split()))

ans = 0

for _ in range(max(h)):
    if h[0]:
        ans += 1
    for i in range(n - 1):
        if not h[i] and h[i + 1]:
            ans += 1
    for j in range(n):
        if h[j]: h[j] -= 1
print(ans)