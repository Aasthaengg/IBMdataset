import bisect


def answer(n: int, m: int, x: int, a: []) -> int:
    i = bisect.bisect_left(a, x)
    return min(i, len(a) - i)


def main():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(answer(n, m, x, a))


if __name__ == '__main__':
    main()