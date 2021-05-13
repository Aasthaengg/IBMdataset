import sys
from collections import defaultdict
from itertools import combinations

input = sys.stdin.readline


def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())

    if N == 1:
        print(1)
        sys.exit()

    vector = defaultdict(int)
    for a, b in combinations(range(N), 2):
        dx = x[a] - x[b]
        dy = y[a] - y[b]
        if dx == 0:
            vector[(0, abs(dy))] += 1
        elif dx > 0:
            vector[(dx, dy)] += 1
        else:
            vector[(-dx, -dy)] += 1

    ans = N - max(vector.values())
    print(ans)


if __name__ == "__main__":
    main()
