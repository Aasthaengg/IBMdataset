N, M = map(int, input().split())
H = [0] + list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

h = [0] * (N + 1)
for i in range(M):
    h[AB[i][0]] = max(h[AB[i][0]], H[AB[i][1]])
    h[AB[i][1]] = max(h[AB[i][1]], H[AB[i][0]])

ans = 0
for i in range(N + 1):
    if h[i] < H[i]:
        ans += 1

print(ans)
