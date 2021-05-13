LI = lambda: list(map(int, input().split()))

W, H, x, y = LI()


def main():
    s = W * H / 2
    if 2 * x == W and 2 * y == H:
        t = 1
    else:
        t = 0
    print(s, t)


if __name__ == "__main__":
    main()
