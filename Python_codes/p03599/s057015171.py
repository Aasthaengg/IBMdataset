import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    A, B, C, D, E, F = map(int, input().split())

    max_deisity = 100 * E / (100 + E)
    MAX = -1
    W = 0
    S = 0
    for a in range(F // (100 * A) + 1):
        rest1 = F - a * A * 100
        for b in range(rest1 // (100 * B) + 1):
            if a == 0 and b == 0:
                continue

            water = a * A * 100 + b * B * 100
            rest2 = F - water
            for c in range(rest2 // C + 1):
                rest3 = rest2 - C * c
                for d in range(rest3 // D + 1):
                    sugar = C * c + D * d

                    if water + sugar > F:
                        continue

                    density = 100 * sugar / (water + sugar)
                    if max_deisity < density:
                        continue

                    if density > MAX:
                        MAX = density
                        W = water
                        S = sugar

    print(W + S, S)


if __name__ == "__main__":
    main()
