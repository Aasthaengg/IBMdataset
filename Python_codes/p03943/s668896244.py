import sys

input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())
    ans = "No"
    if a == b + c:
        ans = "Yes"
    if b == c + a:
        ans = "Yes"
    if c == a + b:
        ans = "Yes"
    print(ans)


if __name__ == "__main__":
    main()
