R, G, B, N = map(int, input().split())
ans = 0
for r in range(N+1):
    for g in range(N+1):
        res = N-R*r-G*g
        if res < 0:
            continue
        else:
            if res%B == 0:
                ans += 1
print(ans)
