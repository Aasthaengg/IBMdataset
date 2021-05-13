def answer(d: int, n: int) -> int:
    if n == 100:
        n += 1
    return 100 ** d * n


def main():
    d, n = map(int, input().split())
    print(answer(d, n))


if __name__ == '__main__':
    main()