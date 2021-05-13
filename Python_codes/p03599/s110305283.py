def solve():
    max_density = -1
    ans = [-1, -1]
    A, B, C, D, E, F = map(int, input().split())
    for a in range(0, F + 1, A * 100):
        for b in range(0, F - a + 1, B * 100):
            w = a + b
            if w == 0:
                continue
            max_s = min(F - w, w // 100 * E)
            for c in range(0, max_s + 1, C):
                for d in range(0, max_s - c + 1, D):
                    s = c + d
                    density = 100 * s / (w + s)
                    if density > max_density:
                        ans = [w + s, s]
                        max_density = density
    return ans


print(*solve())
