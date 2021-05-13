import sys

input = sys.stdin.readline


def main():
    R = int(input())
    G = int(input())

    # (R + x) / 2 = G
    # x = 2G - R
    ans = 2 * G - R

    print(ans)


if __name__ == "__main__":
    main()
