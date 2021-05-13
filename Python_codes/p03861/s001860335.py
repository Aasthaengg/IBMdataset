def answer(a: int, b: int, x: int) -> int:
    return b // x - (a - 1) // x


def main():
    a, b, x = map(int, input().split())
    print(answer(a, b, x))


if __name__ == '__main__':
    main()