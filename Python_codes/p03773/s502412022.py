#!python3

LI = lambda: list(map(int, input().split()))

# input
A, B = LI()


def main():
    ans = (A + B) % 24
    print(ans)


if __name__ == "__main__":
    main()
