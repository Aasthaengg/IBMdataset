#!python3

LI = lambda: list(map(int, input().split()))

# input
a, b, x = LI()


def main():
    if a % x == 0:
        v = a
    else:
        v = (a // x + 1) * x
    if v > b:
        ans = 0
    else:
        ans = (b - v) // x + 1
    print(ans)


if __name__ == "__main__":
    main()
