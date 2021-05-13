def answer(n: int, m: int, a: []) -> int:
    return max(-1, n - sum(a))


def main():
    n, m = map(int, input().split())
    a = map(int, input().split())
    print(answer(n, m, a))


if __name__ == '__main__':
    main()