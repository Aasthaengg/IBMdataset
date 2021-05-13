import sys

input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    ans = sum(a[:2 * N][1::2])

    print(ans)


if __name__ == "__main__":
    main()
