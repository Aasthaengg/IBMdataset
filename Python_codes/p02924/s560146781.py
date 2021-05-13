import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    N = int(readline())

    print(N * (N - 1) // 2)


if __name__ == "__main__":
    main()
