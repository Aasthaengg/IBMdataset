from math import ceil


def main():
    N, D = map(int, input().split())
    print(ceil(N / (2*D + 1)))


if __name__ == '__main__':
    main()
