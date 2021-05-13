from math import ceil


def main():
    numbers = list(map(int, input().split()))
    print(ceil(sum(numbers) / 2))


if __name__ == '__main__':
    main()