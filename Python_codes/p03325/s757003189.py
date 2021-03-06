import sys

input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in a:
        while True:
            if i % 2 == 0:
                ans += 1
                i //= 2
            else:
                break

    print(ans)


if __name__ == "__main__":
    main()
