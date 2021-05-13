import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()
    S = S.replace(",", " ")
    print(S)


if __name__ == "__main__":
    main()
