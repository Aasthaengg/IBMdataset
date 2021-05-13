def exchange(a, b, c):
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        return 0

    if a == b == c:
        return -1

    return exchange((b + c) / 2, (c + a) / 2, (a + b) / 2) + 1


def main():
    a, b, c = map(int, input().split())

    ans = exchange(a, b, c)

    print(ans)


if __name__ == "__main__":
    main()
