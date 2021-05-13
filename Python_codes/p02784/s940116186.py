def answer(h: int, n: int, a: []) -> str:
    return 'Yes' if h <= sum(a) else 'No'


def main():
    h, n = map(int, input().split())
    a = map(int, input().split())
    print(answer(h, n, a))


if __name__ == '__main__':
    main()
