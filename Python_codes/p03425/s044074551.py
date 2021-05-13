import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n = int(input().rstrip())
    s = [input()[0] for _ in range(n)]
    s = [v for v in s if v in 'MARCH']
    c = Counter(s)
    ans = 0
    for x, y, z in combinations(c, 3):
        ans += c[x] * c[y] * c[z]
    print(ans)


if __name__ == '__main__':
    main()
