import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())

    # N(N+1)/2 - X = a
    # (N+1)(N+2)/2 - X = b
    for i in range(1, 999):
        Xa = i * (i + 1) // 2 - a
        Xb = (i + 1) * (i + 2) // 2 - b
        if Xa == Xb:
            ans = Xa
            break

    print(ans)


if __name__ == "__main__":
    main()
