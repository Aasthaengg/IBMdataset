import sys
input = sys.stdin.readline


def main():
    K, X = map(int, input().split())
    print("Yes") if 500*K >= X else print("No")


if __name__ == '__main__':
    main()
