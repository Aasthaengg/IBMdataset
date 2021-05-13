#!python3

LI = lambda: list(map(int, input().split()))

# input
A, B, C, D, E, F = LI()


def main():
    ans = (0, 0, 0)
    for b in range(F // 100 // B + 1):
        water = 100 * B * b
        for a in range((F - water) // 100 // A + 1):
            water += 100 * A * a
            if water == 0:
                continue
            # 砂糖の許容量
            s = min(F - water, water // 100 * E)
            for d in range(s // D + 1):
                sugar = d * D
                sugar += (s - sugar) // C * C
                t = (sugar / (water + sugar), water + sugar, sugar)
                if ans < t:
                    ans = t
    print(*ans[1:])


if __name__ == "__main__":
    main()
