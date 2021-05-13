def answer(n: int, a: []) -> int:
    return max(a) - min(a)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(n, a))


if __name__ == '__main__':
    main()