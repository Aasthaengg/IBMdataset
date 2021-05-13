BILLS = [10000, 5000, 1000]


def calc_price(counts):
    return sum([bill * count for bill, count in zip(BILLS, counts)])


def main(n, y):
    for c1 in range(n + 1):
        for c2 in range(0, n - c1 + 1):
            counts = [c1, c2, n - c1 - c2]
            if calc_price(counts) == y:
                print(' '.join([str(c) for c in counts]))
                return
    print('-1 -1 -1')


if __name__ == "__main__":
    n, y = [int(x) for x in input().split()]
    main(n, y)
