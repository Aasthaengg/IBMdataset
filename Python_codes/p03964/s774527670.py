def ceil(x, y):
    # ceil(x / y)
    return (x + y - 1) // y


def main():
    n = int(input())
    takahashi = 1
    aoki = 1
    for _ in range(n):
        t, a = map(int, input().split())
        diff = max(ceil(takahashi, t), ceil(aoki, a))
        takahashi = t * diff
        aoki = a * diff
    print(takahashi + aoki)


if __name__ == '__main__':
    main()
