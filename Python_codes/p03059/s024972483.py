LI = lambda: list(map(int, input().split()))

A, B, T = LI()


def main():
    ans = (T // A) * B
    print(ans)


if __name__ == "__main__":
    main()
