N = int(input())
P = list(map(int, input().split()))

ans = 0

for i in range(N):
    p = P[i]
    if p == i + 1:
        ans += 1
        if i < N - 1:
            P[i], P[i + 1] = P[i + 1], P[i]
        else:
            P[i], P[i - 1] = P[i - 1], P[i]

print(ans)