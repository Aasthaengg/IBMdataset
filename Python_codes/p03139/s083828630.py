import sys


def main():
    raw = input().split(' ')
    n = int(raw[0])
    a = int(raw[1])
    b = int(raw[2])

    def get_max():
        return min(a, b)

    def get_min():
        return max(a + b - n, 0)

    print("{} {}".format(get_max(), get_min()))


if __name__ == "__main__":
    argv = sys.argv[1:]
    main()
