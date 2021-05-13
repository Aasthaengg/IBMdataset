import sys
from itertools import combinations

input = sys.stdin.readline


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    ans = "Yay!"
    for p, q in combinations([a, b, c, d, e], 2):
        if abs(p - q) > k:
            ans = ":("

    print(ans)


if __name__ == "__main__":
    main()
