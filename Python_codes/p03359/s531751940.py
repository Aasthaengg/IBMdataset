LI = lambda: list(map(int, input().split()))

a, b = LI()


def main():
    ans = a - 1 if b < a else a
    print(ans)


if __name__ == "__main__":
    main()
