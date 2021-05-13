import sys

input = sys.stdin.readline


def main():
    N = int(input())

    ans = str(N).count("2")
    print(ans)


if __name__ == "__main__":
    main()
