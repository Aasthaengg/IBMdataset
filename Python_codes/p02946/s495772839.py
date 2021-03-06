def answer(k: int, x: int) -> str:
    may_be_black = map(str, range(x - k + 1, x + k))
    return ' '.join(may_be_black)


def main():
    k, x = map(int, input().split())
    print(answer(k, x))


if __name__ == '__main__':
    main()