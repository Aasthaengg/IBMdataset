R, G, B, N = map(int, input().split())
ans = 0
for r in range(3001):
    n = N - (r * R)
    if n < 0:
        break
    for g in range(3001):
        nn = n - (g * G)
        if nn < 0:
            break
        elif nn % B == 0:
            ans += 1

print(ans)
