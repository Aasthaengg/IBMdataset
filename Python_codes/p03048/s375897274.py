R, G, B, N = map(int, input().split())
ans = 0
r=0
while r*R <= N:
    g=0
    while r*R + g*G <= N:
        if (N - r*R - g*G) % B == 0:
            ans += 1
        g += 1
    r += 1
print(ans)
