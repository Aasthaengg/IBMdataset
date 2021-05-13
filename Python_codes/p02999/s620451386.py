LI = lambda: list(map(int, input().split()))

X, A = LI()


def main():
    ans = 0 if X < A else 10
    print(ans)


if __name__ == "__main__":
    main()
