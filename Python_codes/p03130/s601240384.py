from collections import defaultdict


def resolve():
    d = defaultdict(int)
    ab = list(list(map(int, input().split())) for _ in range(3))
    for a, b in ab:
        d[a] += 1
        d[b] += 1
    print("YES" if set(d.keys()) == {1, 2, 3, 4} and all(v < 3 for v in d.values()) else "NO")


if __name__ == "__main__":
    resolve()
