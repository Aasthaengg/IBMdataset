R, G, B, N = map(int, input().split())

ans = 0

for g in range(N//G+1):
    for b in range(N//B+1):
        s = N-g*G-b*B
        if s < 0:
            break
        if s%R == 0:
            ans += 1

print(ans)