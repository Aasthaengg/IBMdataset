import sys

input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())

    price = [a, b, c]
    price.sort()
    ans = price[0] + price[1]

    print(ans)


if __name__ == "__main__":
    main()
