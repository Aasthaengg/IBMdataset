LI = lambda: list(map(int, input().split()))

N = input()


def main():
    if N[0] == N[2]:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)


if __name__ == "__main__":
    main()
