from collections import Counter


def main():
    S = input()

    c = Counter(S)

    if len(c) == 2 and list(c.values())[0] == 2 and list(c.values())[1] == 2:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
