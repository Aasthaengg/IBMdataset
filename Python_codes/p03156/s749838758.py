def main(n, a, b, p):
    _a, _ab, _b = 0, 0, 0

    for p in p:
        if p <= a:
            _a += 1
        elif a < p <= b:
            _ab += 1
        elif p > b:
            _b += 1

    print(min(_a, _ab, _b))


if __name__ == "__main__":
    n = int(input())
    a, b = map(int, input().split())
    p = list(map(int, input().split()))

    main(n, a, b, p)
