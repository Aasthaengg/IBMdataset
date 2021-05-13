import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    H.sort()
    if K == 0:
        ans = sum(H)
    else:
        ans = sum(H[:-K])

    print(ans)


if __name__ == "__main__":
    main()
