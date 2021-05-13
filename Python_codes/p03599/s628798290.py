import sys
def input(): return sys.stdin.readline().strip()

def main():
    A, B, C, D, E, F = map(int, input().split())
    weight = 0.1
    sugar = 0

    for p in range(F // (100 * A) + 1):
        for q in range(0, (F - 100 * A * p) // (100 * B) + 1):
            upper = (A * p + B * q) * E
            water = (A * p + B * q) * 100
            if water == 0: continue
            for r in range(0, upper // C + 1):
                if water + C * r > F: continue
                s = (upper - C * r) // D
                while s >= 0 and water + C * r + D * s > F: s -= 1
                if s < 0: continue
                if sugar * (water + C * r + D * s) < (C * r + D * s) * weight:
                    weight = water + C * r + D * s
                    sugar = C * r + D * s
    if sugar == 0:
        print("{} 0".format(100 * A))
    else:
        print("{} {}".format(weight, sugar))

    


if __name__ == "__main__":
    main()
