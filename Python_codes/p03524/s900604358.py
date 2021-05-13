import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    a = S.count("a")
    b = S.count("b")
    c = S.count("c")

    if abs(a - b) <= 1 and abs(b - c) <= 1 and abs(c - a) <= 1:
        ans = "YES"
    else:
        ans = "NO"

    print(ans)


if __name__ == "__main__":
    main()
