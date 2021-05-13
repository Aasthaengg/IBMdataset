import sys
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    t = 100 * n + 1800 * m
    print(t * pow(2, m))


if __name__ == "__main__":
    main()
