import sys
def input(): return sys.stdin.readline().strip()


def main():
    a, b, c, d = map(int, input().split())
    print(max(a * b, c * d))


if __name__ == "__main__":
    main()
