
def answer(n: int, k: int, h: []) -> int:
    return len(list(i for i in h if k <= i))


def main():
    n, k = map(int, input().split())
    h = map(int, input().split())
    print(answer(n, k, h))


if __name__ == '__main__':
    main()
