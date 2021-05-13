LI = lambda: list(map(int, input().split()))

S = input()


def main():
    n = len(S)
    sn = len(set(S))
    ans = "yes" if sn == n else "no"
    print(ans)


if __name__ == "__main__":
    main()
