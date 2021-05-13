import sys
def input(): return sys.stdin.readline().strip()


def main():
    A, B, C = map(int, input().split())
    print(min(B // A, C))


if __name__ == "__main__":
    main()
