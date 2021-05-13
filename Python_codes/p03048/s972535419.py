R,G,B,N = map(int, input().split())

ans = 0
for r in range(0, N+1, R):
    for g in range(0, N+1-r, G):
        if (N-r-g)%B == 0:
            ans += 1
print(ans)