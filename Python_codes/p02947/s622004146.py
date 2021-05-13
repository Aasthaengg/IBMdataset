import collections


def main():
    n = int(input())
    print(sum(cVal * (cVal - 1) // 2 for cVal in collections.Counter(
        [''.join(sorted(list(input()))) for _ in range(n)]).values()))


if __name__ == '__main__':
    main()
