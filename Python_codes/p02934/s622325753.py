def main() -> None:
    _ = int(input())
    A = [int(x) for x in input().split()]
    s = sum(1 / a for a in A)
    print("{:.015f}".format(1 / s))


if __name__ == '__main__':
    main()
