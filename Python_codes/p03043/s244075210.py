N, K = map(int, input().split())
ans = 0
for i in range(1, N+1):
    prob = 1 / N
    for _ in range(20):
        if i >= K:
            ans += prob
            break
        i *= 2
        prob /= 2
print(ans)