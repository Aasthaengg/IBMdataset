import math


def resolve():
    n, k = map(int, input().split())
    print("YES" if k <= math.ceil(n / 2) else "NO")


if __name__ == "__main__":
    resolve()
