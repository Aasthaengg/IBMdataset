LI = lambda: list(map(int, input().split()))

A, B = LI()


def main():
    ans = A + B;
    if ans >= 10:
        ans = "error"
    print(ans)


if __name__ == "__main__":
    main()
