import sys
input = sys.stdin.readline


def main():
    x = int(input())
    rank = 10 - x // 200
    print(rank)


if __name__ == "__main__":
    main()
