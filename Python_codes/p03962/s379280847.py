import sys

input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())

    ans = 3
    if a == b == c:
        ans = 1
    else:
        if a == b:
            ans -= 1
        if b == c:
            ans -= 1
        if c == a:
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
