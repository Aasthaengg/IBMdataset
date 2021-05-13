R, G, B, N = map(int, input().split())

ans = 0
for r in range(0, N+1, 1):
    for g in range(0, N+1 - R*r, 1):
        if N - R*r - G*g < 0:
            continue
        elif (N - R*r - G*g) % B == 0:
            ans += 1
print(ans)