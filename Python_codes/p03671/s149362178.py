import sys
def input(): return sys.stdin.readline().strip()


def main():
    a, b, c = map(int, input().split())
    m = max(a, b, c)
    print(a + b + c - m)


if __name__ == "__main__":
    main()
