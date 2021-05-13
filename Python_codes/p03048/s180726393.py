def solve():
    R, G, B, N = map(int, input().split())
    LIM = 3001
    ans = 0
    for r in range(LIM):
        for g in range(LIM):
            if R * r + G * g > N:
                break
            Bb = N - R * r - G * g
            if Bb % B == 0:
                ans += 1
    return ans


print(solve())
