import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    ans = (S.count("g") - S.count("p")) // 2

    print(ans)


if __name__ == "__main__":
    main()
