def main() -> None:
    a, b, c, d = map(lambda x: int(x), input().split())
    print(max(a * c, a * d, b * c, b * d))


if __name__ == '__main__':
    main()
