LI = lambda: list(map(int, input().split()))

A, P = LI()


def main():
    ans = (3 * A + P) // 2
    print(ans)


if __name__ == "__main__":
    main()
