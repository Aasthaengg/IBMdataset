from itertools import permutations
from math import factorial


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for p in permutations(range(n), n):
        dist = 0
        for i in range(len(p) - 1):
            dist += (abs(xy[p[i]][0] - xy[p[i + 1]][0]) ** 2 +
                     abs(xy[p[i]][1] - xy[p[i + 1]][1]) ** 2) ** 0.5
        ans += dist

    ans /= factorial(n)

    print(f"{ans:.12f}")


if __name__ == "__main__":
    main()
