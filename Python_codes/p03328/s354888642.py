import sys
def input(): return sys.stdin.readline().strip()


def main():
    a, b = map(int, input().split())
    c = b - a
    print(c * (c + 1) // 2 - b)


if __name__ == "__main__":
    main()
