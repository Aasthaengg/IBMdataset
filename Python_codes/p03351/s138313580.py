import sys

input = sys.stdin.readline


def main():
    a, b, c, d = map(int, input().split())

    ab = abs(a - b) <= d
    bc = abs(b - c) <= d
    ca = abs(c - a) <= d
    if ca or (ab and bc):
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
