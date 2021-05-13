import sys

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    ans = H * W - H * w - (W - w) * h
    print(ans)


if __name__ == "__main__":
    main()
